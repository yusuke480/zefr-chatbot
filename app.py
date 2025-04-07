# -*- coding: utf-8 -*-
import random
import streamlit as st
from difflib import get_close_matches

def zefr_chatbot(user_input):
    user_input = user_input.lower()

    faq = {
        "zefrとは": "ZefrはYouTube向けのコンテキスト広告プラットフォームです。ブランドセーフティと適切なコンテンツマッチングを提供します。",
        "何ができる": "Zefrは動画コンテンツをAIで解析し、ブランドに最適な広告枠を提案します。ブランドセーフ、スケーラブル、精度の高いターゲティングが可能です。",
        "使い方": "Zefrの導入には、YouTube広告アカウントとの連携が必要です。Zefrチームがキャンペーン設計から実行までサポートします。",
        "料金": "料金は広告出稿金額に応じた従量課金制が基本ですが、年間契約などのプランもあります。詳細は営業担当までご相談ください。",
        "zefrの強み": "Zefrの強みは、AIを用いたコンテンツ解析による精度の高いマッチングと、第三者機関による検証済みのブランドセーフ環境の提供です。",
        "他社との違い": "Zefrは視聴者ターゲティングではなく、コンテンツターゲティングに強みを持っています。他社DSPやDMPと異なり、YouTubeに特化して高精度な枠選定が可能です。",
        "どのような業種に向いている": "ZefrはFMCG、エンタメ、自動車、飲料など、ブランドセーフティが求められる幅広い業種に適しています。",
        "レポート内容": "Zefrでは、出稿枠のURLリストや視聴されたコンテンツのカテゴリ、ブランドセーフ指標などの詳細レポートを提供します。",
        "YouTube Shortsにも対応している？": "はい、ZefrはYouTube Shortsにも対応しており、ショート動画特有のコンテンツ解析とマッチングが可能です。",
        "ターゲティングの方法": "Zefrでは、視聴ユーザーではなく、動画コンテンツそのものの文脈に基づいたターゲティングを行います。AIがコンテンツを解析し、適切な動画を選定します。",
        "zefrはどうやってコンテンツを解析しているの？": "Zefrは動画内の音声・映像・テキストをAIと機械学習で分析し、コンテンツのジャンルやトーン、ブランド適合性を判定します。",
        "zefrはyoutube以外でも使える？": "現在、ZefrはYouTube広告に特化しており、他のプラットフォームでの利用は制限されています。",
        "zefrは日本語コンテンツにも対応してるの？": "はい、Zefrは日本語を含む多言語に対応しており、日本市場向けのコンテンツにも対応可能です。",
        "zefrの効果は？": "広告のビューアビリティ、ブランド適合性、エンゲージメント率の向上が報告されています。特にブランドセーフティの確保が強みです。",
        "どんな業界で使われてる？": "消費財、エンタメ、通信、自動車など多くの業界で導入されています。",
        "導入までにどのくらい時間がかかる？": "初回ミーティングから設定完了までは通常1〜2週間程度です。",
        "zefrチームのサポートはある？": "はい、専任担当がキャンペーン設計から運用・レポーティングまでをサポートします。",
        "広告代理店と連携して使える？": "もちろん可能です。ZefrはGoogle認定のパートナーで、代理店との連携体制も整っています。"
    }

    question_keys = list(faq.keys())
    best_match = get_close_matches(user_input, question_keys, n=1, cutoff=0.5)

    if best_match:
        return faq[best_match[0]]

    fallback_responses = [
        "すみません、それについてはまだ学習していませんが、Zefrの営業担当に確認することをおすすめします。",
        "その点については、もう少し詳しく教えていただけますか？",
        "Zefrの詳しい資料をご覧いただくか、お問い合わせください。"
    ]

    return random.choice(fallback_responses)

# Streamlit GUI
st.set_page_config(page_title="Zefr Chatbot", layout="centered")

# Zefrロゴ表示（正しいGitHub Raw URL + 推奨パラメータ）
st.image("https://raw.githubusercontent.com/yusukefukuoka/zefr-chatbot/main/zefr-dmp-data-CONTENT-2019-652x367.jpg", use_container_width=True)

st.title("💬 Zefr Chatbot")
st.markdown("---")

user_input = st.text_input("🧑‍💻 Zefrに関する質問を入力してください：")

if user_input:
    response = zefr_chatbot(user_input)
    st.markdown(f"#### 🤖 Zefr Botの回答：")
    st.write(response)
