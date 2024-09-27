import sys
from pathlib import Path
from maa.toolkit import Toolkit
from maa.context import Context
from maa.custom_action import CustomAction
from maa.custom_recognition import CustomRecognition


def main():
    # 注册自定义动作
    Toolkit.pi_register_custom_action("MyAct", MyAction())
    # 注册自定义识别器
    Toolkit.pi_register_custom_recognition("MyRec", MyRecongition())
    # 查找MaaPiCli并启动
    start_cli()


def start_cli():
    # 打包后Path(__file__)获取的路径会更改，详见build.py中PyInstaller.__main__.run()处注释
    working_path = Path(__file__)
    root_path = working_path.parent.parent
    # 测试用
    root_path = Path(__file__).parent.parent.parent / "install"
    # 查找包含 MaaPiCli.exe 的路径
    result = root_path.rglob("MaaPiCli.exe")
    try:
        pi_cli_path = next(result)
    except StopIteration:
        print("未找到包含 MaaPiCli.exe 的路径.")
        input("按任意键退出...")
        # exit()打包后会出现异常, 应使用sys.exit()终止程序的执行
        sys.exit(1)
    # 启动 MaaPiCli
    Toolkit.pi_run_cli(pi_cli_path.parent, pi_cli_path.parent / "cache", False)


class MyAction(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult:

        print(f"on MyAction.run, context: {context}, argv: {argv}")

        context.override_next(argv.current_task_name, [])

        image = context.tasker.controller.cached_image
        context.tasker.controller.post_click(100, 100).wait()

        return CustomAction.RunResult(success=True)


class MyRecongition(CustomRecognition):

    def analyze(
        self,
        context,
        argv: CustomRecognition.AnalyzeArg,
    ) -> CustomRecognition.AnalyzeResult:
        reco_detail = context.run_recognition(
            "MyCustomOCR",
            argv.image,
            pipeline_override={"MyCustomOCR": {"roi": [100, 100, 200, 300]}},
        )

        # context is a reference, will override the pipeline for whole task
        context.override_pipeline({"MyCustomOCR": {"roi": [1, 1, 114, 514]}})
        # context.run_recognition ...

        # make a new context to override the pipeline, only for itself
        new_context = context.clone()
        new_context.override_pipeline({"MyCustomOCR": {"roi": [100, 200, 300, 400]}})
        reco_detail = new_context.run_recognition("MyCustomOCR", argv.image)

        click_job = context.tasker.controller.post_click(10, 20)
        click_job.wait()

        context.override_next(argv.current_task_name, [])

        return CustomRecognition.AnalyzeResult(
            box=(0, 0, 100, 100), detail="Hello World!"
        )


if __name__ == "__main__":
    main()
