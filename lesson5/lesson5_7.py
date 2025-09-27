from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import gradio as gr
import time

# 初始化模型
model = OllamaLLM(model="gemma3:1b")

# 建立多變數的翻譯模板
complex_template = """
你是一位專業的{target_language}翻譯家，專精於{domain}領域。
請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣和風格
2. 使用專業術語
3. 符合{target_language}的語言習慣

{source_language}文本：{text}
{target_language}翻譯：
"""

chat_prompt_template = ChatPromptTemplate.from_template(complex_template)

# 翻譯函數
def translate_text(source_language, target_language, domain, text):
    """
    執行翻譯的函數
    """
    if not text.strip():
        return "請輸入要翻譯的文本！"
    
    try:
        # 格式化提示模板
        formatted_prompt = chat_prompt_template.format(
            target_language=target_language,
            source_language=source_language,
            domain=domain,
            text=text
        )
        
        # 調用模型進行翻譯
        response = model.invoke(formatted_prompt)
        return response
        
    except Exception as e:
        return f"翻譯過程中發生錯誤：{str(e)}"

# 自定義 CSS 樣式
custom_css = """
/* 主要容器樣式 */
.gradio-container {
    font-family: 'Microsoft JhengHei', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

/* 標題樣式 */
.title {
    color: #ffffff;
    text-align: center;
    font-size: 2.5em;
    font-weight: bold;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

/* 描述文字樣式 */
.description {
    color: #f0f0f0;
    text-align: center;
    font-size: 1.2em;
    margin-bottom: 30px;
    line-height: 1.6;
}

/* 輸入框樣式 */
.textbox textarea {
    border-radius: 15px !important;
    border: 2px solid #e0e0e0 !important;
    padding: 15px !important;
    font-size: 16px !important;
    background-color: #ffffff !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
}

/* 下拉選單樣式 */
.dropdown {
    border-radius: 10px !important;
    border: 2px solid #e0e0e0 !important;
    background-color: #ffffff !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
}

/* 按鈕樣式 */
.button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4) !important;
    border: none !important;
    border-radius: 25px !important;
    color: white !important;
    font-weight: bold !important;
    padding: 12px 30px !important;
    font-size: 16px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    transition: all 0.3s ease !important;
}

.button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
}

/* 輸出框樣式 */
.output-text {
    border-radius: 15px !important;
    border: 2px solid #4ECDC4 !important;
    background-color: #f8fffe !important;
    padding: 20px !important;
    font-size: 16px !important;
    line-height: 1.8 !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
}

/* 卡片樣式 */
.panel {
    background-color: rgba(255,255,255,0.95) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1) !important;
    backdrop-filter: blur(10px) !important;
}
"""

# 建立 Gradio 介面
def create_interface():
    with gr.Blocks(css=custom_css, title="AI 專業翻譯助手") as demo:
        gr.HTML("""
        <div class="title">🌍 AI 專業翻譯助手</div>
        <div class="description">
            使用先進的 AI 技術，提供專業、準確的多語言翻譯服務<br>
            支援多種語言和專業領域，讓您的溝通無障礙
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.HTML('<div class="panel">')
                
                # 語言選擇
                source_lang = gr.Dropdown(
                    choices=["英文", "日文", "韓文", "法文", "德文", "西班牙文", "義大利文"],
                    value="英文",
                    label="🌐 源語言",
                    info="選擇要翻譯的原始語言"
                )
                
                target_lang = gr.Dropdown(
                    choices=["繁體中文", "簡體中文", "英文", "日文", "韓文", "法文", "德文", "西班牙文", "義大利文"],
                    value="繁體中文",
                    label="🎯 目標語言",
                    info="選擇翻譯後的目標語言"
                )
                
                # 領域選擇
                domain = gr.Dropdown(
                    choices=["商業", "科技", "醫學", "法律", "教育", "文學", "新聞", "日常對話"],
                    value="商業",
                    label="📚 專業領域",
                    info="選擇文本所屬的專業領域"
                )
                
                gr.HTML('</div>')
                
            with gr.Column(scale=2):
                gr.HTML('<div class="panel">')
                
                # 輸入文本
                input_text = gr.Textbox(
                    label="📝 輸入要翻譯的文本",
                    placeholder="請在此輸入您要翻譯的內容...",
                    lines=8,
                    info="支援長文本翻譯，請輸入完整的句子或段落"
                )
                
                # 翻譯按鈕
                translate_btn = gr.Button(
                    "🚀 開始翻譯",
                    variant="primary",
                    size="lg"
                )
                
                # 輸出結果
                output_text = gr.Textbox(
                    label="✨ 翻譯結果",
                    lines=8,
                    interactive=False,
                    info="AI 將為您提供專業、準確的翻譯結果"
                )
                
                gr.HTML('</div>')
        
        # 範例文本
        gr.HTML('<div class="panel">')
        gr.Examples(
            examples=[
                ["英文", "繁體中文", "商業", "The quarterly revenue increased by 15% compared to last year."],
                ["英文", "繁體中文", "科技", "Artificial intelligence is revolutionizing the way we work and live."],
                ["日文", "繁體中文", "日常對話", "こんにちは、元気ですか？"],
                ["韓文", "繁體中文", "教育", "학습은 평생의 과정입니다."]
            ],
            inputs=[source_lang, target_lang, domain, input_text],
            label="💡 點擊下方範例快速開始"
        )
        gr.HTML('</div>')
        
        # 事件綁定
        translate_btn.click(
            fn=translate_text,
            inputs=[source_lang, target_lang, domain, input_text],
            outputs=output_text,
            show_progress=True
        )
        
        # 快速翻譯（按 Enter）
        input_text.submit(
            fn=translate_text,
            inputs=[source_lang, target_lang, domain, input_text],
            outputs=output_text
        )
    
    return demo

# 啟動介面
if __name__ == "__main__":
    demo = create_interface()
    print("🚀 正在啟動 AI 翻譯助手...")
    print("📱 介面將在瀏覽器中自動開啟")
    print("🌐 如果沒有自動開啟，請複製下方網址到瀏覽器：")
    
    demo.launch(
        share=True,  # 創建公開連結
        server_name="0.0.0.0",  # 允許外部訪問
        server_port=7860,  # 指定端口
        show_error=True,  # 顯示錯誤信息
        quiet=False,  # 顯示啟動信息
        favicon_path=None  # 使用默認圖標
    )