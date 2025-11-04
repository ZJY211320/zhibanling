import gradio as gr

def modelscope_quickstart(name):
    coze_home = "https://www.coze.cn"
    guide = f"""
    欢迎使用智伴龄应用，{name}！<br><br>
    请按以下步骤使用：<br>
    1. 点击链接进入扣子平台：<a href='{coze_home}' target='_blank'>{coze_home}</a><br>
    2. 用手机号登录/注册账号<br>
    3. 点击开发平台，进入左侧「模板商店」<br>
    4. 在搜索栏输入「智伴龄」并点击搜索结果使用<br>
    """
    return guide

demo = gr.Interface(
    fn=modelscope_quickstart,
    inputs="text",
    outputs=gr.HTML()
)
demo.launch()