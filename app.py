import streamlit as st

st.set_page_config(
    page_title="김덕건 - 자기소개",
    page_icon="👨‍💻",
    layout="wide",
)

st.markdown("""
<style>
    .main { background-color: #0f0f1a; }
    .block-container { padding-top: 2rem; }
    h1, h2, h3 { color: #a0aaff; }
    .hero-box {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #1a1a3e, #0d2040);
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid rgba(100,120,255,0.2);
    }
    .hero-name {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #6478ff, #00c8b4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        border: 1px solid rgba(100,120,255,0.4);
        font-size: 0.9rem;
        color: #a0aaff;
        background: rgba(100,120,255,0.08);
        margin: 0.3rem;
    }
    .info-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .info-label {
        font-size: 0.75rem;
        color: #6478ff;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.3rem;
    }
    .info-value {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e0e0f0;
    }
    .intro-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.5rem;
        line-height: 2;
        font-size: 1.05rem;
        color: #c0c8e8;
    }
    .tl-item {
        border-left: 2px solid #6478ff;
        padding-left: 1.5rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    .tl-year { color: #6478ff; font-size: 0.85rem; margin-bottom: 0.2rem; }
    .tl-title { font-size: 1rem; font-weight: 600; color: #e0e0f0; }
    .tl-desc { font-size: 0.9rem; color: #8890cc; margin-top: 0.2rem; }
    .contact-btn {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(100,120,255,0.3);
        background: rgba(100,120,255,0.06);
        color: #a0aaff;
        text-decoration: none;
        margin-right: 0.8rem;
        font-size: 0.95rem;
    }
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #a0aaff;
        border-bottom: 1px solid rgba(100,120,255,0.3);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6478ff, #00c8b4);
    }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero-box">
    <div style="font-size:4rem; margin-bottom:1rem;">👨‍💻</div>
    <div class="hero-name">김덕건</div>
    <div style="color:#8890cc; font-size:1.2rem; margin-top:0.4rem;">Developer</div>
    <div style="margin-top:1.2rem;">
        <span class="badge">💻 개발자</span>
        <span class="badge">🔥 30년+ 경력</span>
        <span class="badge">🚀 끊임없는 성장</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ABOUT ──
st.markdown('<div class="section-title">👤 기본 정보</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">이름</div>
        <div class="info-value">김덕건</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">직업</div>
        <div class="info-value">소프트웨어 개발자</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">관심 분야</div>
        <div class="info-value">웹 개발 · 시스템 설계</div>
    </div>
    """, unsafe_allow_html=True)

# ── INTRO ──
st.markdown('<div class="section-title">💬 소개</div>', unsafe_allow_html=True)
st.markdown("""
<div class="intro-box">
    안녕하세요, 저는 <strong style="color:#a0aaff;">김덕건</strong>입니다.<br>
    오랜 현장 경험을 바탕으로 효율적이고 안정적인 소프트웨어를 개발하는 것을 목표로 합니다.<br>
    새로운 기술을 꾸준히 학습하며, 팀과 함께 성장하는 것을 가장 큰 가치로 생각합니다.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── SKILLS ──
st.markdown('<div class="section-title">🛠 기술 스택</div>', unsafe_allow_html=True)

skills = [
    ("웹 개발 (HTML/CSS/JS)", 90),
    ("백엔드 개발", 85),
    ("데이터베이스 (SQL)", 80),
    ("시스템 설계 / 아키텍처", 88),
    ("문제 해결 능력", 95),
]

for name, pct in skills:
    col_label, col_bar = st.columns([1, 4])
    with col_label:
        st.markdown(f"<div style='color:#c0c8e8; padding-top:0.5rem;'>{name}</div>", unsafe_allow_html=True)
    with col_bar:
        st.progress(pct / 100, text=f"{pct}%")

st.markdown("<br>", unsafe_allow_html=True)

# ── CAREER ──
st.markdown('<div class="section-title">📌 경력 타임라인</div>', unsafe_allow_html=True)

career = [
    ("현재", "소프트웨어 개발자", "웹/시스템 개발 및 유지보수, 팀 리드 역할 수행"),
    ("2010s", "시니어 개발자", "대규모 프로젝트 설계 및 개발 주도"),
    ("2000s", "개발자 경력 시작", "소프트웨어 개발 입문 및 다양한 프로젝트 참여"),
]

for year, title, desc in career:
    st.markdown(f"""
    <div class="tl-item">
        <div class="tl-year">{year}</div>
        <div class="tl-title">{title}</div>
        <div class="tl-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── CONTACT ──
st.markdown('<div class="section-title">📬 연락처</div>', unsafe_allow_html=True)
st.markdown("""
<a class="contact-btn" href="mailto:dgkim91@gmail.com">📧 dgkim91@gmail.com</a>
<a class="contact-btn" href="https://github.com/dgkim-91" target="_blank">🐙 GitHub</a>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; color:#444466; font-size:0.85rem; border-top:1px solid rgba(255,255,255,0.05); padding-top:1.5rem;'>© 2026 김덕건. Made with ❤️</div>",
    unsafe_allow_html=True,
)
