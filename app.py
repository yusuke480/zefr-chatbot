# -*- coding: utf-8 -*-
import random
import streamlit as st
from difflib import get_close_matches
import base64

def zefr_chatbot(user_input):
    user_input = user_input.lower()

    faq = {
        "zefrとは": "ZefrはYouTube向けのコンテキスト広告プラットフォームです。ブランドセーフティと適切なコンテキストマッチングを提供します。",
        "openslateと競合するケースは？": "Openslateが日本で本格展開していないため、グローバル広告主でない限り比較されることは少ないです。",
        "openslateとの違い": "Openslateはチャンネル単位解析、Zefrはビデオ単位。Zefrは1時間ごとにリスト更新、Google Ads・DV360両方で利用可です。",
        "予算延長や増額時の手続き": "Google広告側の設定変更のみで可能ですが、申込書の再提出が必要な場合は対応可能です。",
        "これまでの最大予算": "月間で最大6,000万円の配信実績があります。",
        "dv360での利用": "現状はカテゴリの除外のみ可能ですが、本国と機能追加について交渉中です。",
        "除外したいチャンネル確認": "ブラックリスト併用やサンプル確認で対応。媒体側で除外も可能です。",
        "zefrと媒体ターゲの優先度": "併用可能。Zefrは粒度が高く、デモグラとの掛け合わせ推奨です。",
        "カテゴリはプリセットのみ？": "カスタムカテゴリ作成はZefrに交渉中。日本では未展開です。",
        "費用体系": "例：Googleネット費用の12％（irep様）、グロス9％（DAC様）など。",
        "導入までのスケジュール": "利用申請から5営業日程度を想定ください。",
        "コメントデータも取ってる？": "はい、コメントなども含めてブランドセーフティ判断に利用しています。",
        "カテゴリ設定の相談": "商材に合わせて代理店と相談しながら設定します。",
        "複数カテゴリで成果は見れる？": "可能ですが、Google広告でキャンペーンを分ける必要あり。推奨はシンプル設計です。",
        "なぜGoogleがZefrのような機能を持たない？": "Googleは汎用サービス提供が目的。Zefrは企業個別対応＋URL単位プレースメント設定が可能。",
        "代理店向けの販売計画": "代理店が販売できるよう展開中。クッキーレス対策としても好評です。",
        "ビジネスモデルは？": "Google広告費に対して10％請求。代理店マージンや請求形態は各社対応です。",
        "契約・運用はLegoliss？": "Legolissが契約窓口となる想定。運用も対応可能でGoogle連携もサポートします。",
        "管理画面の操作": "Google Ads または DV360での運用で、代理店が管理画面を操作します。Zefr側は承認とリスト提供を行います。"
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

# CSSで背景グラデーションと文字色変更
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #20e2d7, #4a90e2);
            color: black;
        }
        .stTextInput > div > div > input {
            color: black;
        }
        h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# Zefrロゴ（小さく表示）
st.image("zefr-dmp-data-CONTENT-2019-652x367.jpg", width=120)

# MBKロゴ（同一フォルダにある前提）
st.image("mbk-digital-logo.png", width=160)

st.title("💬 Zefr Chatbot")
st.markdown("---")

user_input = st.text_input("🧑‍💻 Zefrに関する質問を入力してください：")

if user_input:
    response = zefr_chatbot(user_input)
    st.markdown(f"#### 🤖 Zefr Botの回答：")
    st.write(response)
