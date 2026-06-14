import streamlit as st


def footer_home():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        .footer-home-wrap {
            margin-top: 2.5rem;
            display: flex;
            justify-content: center;
        }
        .footer-home-pill {
            background: linear-gradient(135deg, #3b44c4 0%, #5865F2 50%, #7b6ef6 100%);
            border-radius: 5rem;
            padding: 1.2rem 3rem;
            text-align: center;
            display: inline-block;
            box-shadow: 0 0 30px rgba(88, 101, 242, 0.5), 0 0 60px rgba(88, 101, 242, 0.2);
            position: relative;
            overflow: hidden;
        }
        .footer-home-pill::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: linear-gradient(
                45deg,
                transparent 30%,
                rgba(255,255,255,0.08) 50%,
                transparent 70%
            );
            animation: shimmer 3s infinite;
        }
        @keyframes shimmer {
            0%   { transform: translateX(-100%) rotate(45deg); }
            100% { transform: translateX(100%) rotate(45deg); }
        }
        .footer-home-title {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.15rem !important;
            color: #ffffff;
            letter-spacing: 0.05em;
            margin: 0 0 4px 0;
            position: relative;
            z-index: 1;
        }
        .footer-home-sub {
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            color: rgba(255,255,255,0.7);
            margin: 0;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            position: relative;
            z-index: 1;
        }
        .blink {
            animation: blink 1s step-end infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50%       { opacity: 0; }
        }
        </style>

        <div class="footer-home-wrap">
            <div class="footer-home-pill">
                <p class="footer-home-title">
                    YOU WALKED IN. AI CLOCKED YOU.<span class="blink"> |</span>
                </p>
                <p class="footer-home-sub">Face · Voice · Vibe — All Recognised</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        .footer-dash-wrap {
            margin-top: 2.5rem;
            text-align: center;
            padding: 1.2rem 2rem;
            background: linear-gradient(135deg, rgba(88,101,242,0.12) 0%, rgba(123,110,246,0.08) 100%);
            border-radius: 2rem;
            border: 1px solid rgba(88, 101, 242, 0.25);
            position: relative;
            overflow: hidden;
        }
        .footer-dash-wrap::after {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #5865F2, #EB459E, #5865F2, transparent);
            animation: borderflow 3s linear infinite;
            background-size: 200% 100%;
        }
        @keyframes borderflow {
            0%   { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
        .footer-dash-title {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1rem !important;
            color: #5865F2;
            letter-spacing: 0.05em;
            margin: 0 0 4px 0;
        }
        .footer-dash-sub {
            font-family: 'Outfit', sans-serif;
            font-size: 0.7rem;
            color: #5865F2;
            opacity: 0.55;
            margin: 0;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        .blink2 {
            animation: blink2 1s step-end infinite;
        }
        @keyframes blink2 {
            0%, 100% { opacity: 1; }
            50%       { opacity: 0; }
        }
        </style>

        <div class="footer-dash-wrap">
            <p class="footer-dash-title">YOU WALKED IN. AI CLOCKED YOU.<span class="blink2"> |</span></p>
            <p class="footer-dash-sub">Face · Voice · Vibe — All Recognised</p>
        </div>
    """, unsafe_allow_html=True)