import requests
import streamlit as st
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(
    page_title="Elite Task Manager",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Helper to load Lottie animations ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_task = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json")

# --- Premium Glassmorphism & Expanded Hover Glow Styling ---
st.markdown(
    """
    <style>
    /* Global Theme & Smooth Transitions */
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #111827 100%);
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Header Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Sleek Sidebar Design */
    section[data-testid="stSidebar"] {
        background-color: #0b0f17;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Glassmorphic Cards Base */
    .glass-card {
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px 24px;
        margin-bottom: 16px;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    /* 6 Unique Hover Glow Variants */
    .glass-card.variant-red:hover {
        border-color: #ef4444;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.25);
        transform: translateY(-2px);
    }
    .glass-card.variant-amber:hover {
        border-color: #f59e0b;
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.25);
        transform: translateY(-2px);
    }
    .glass-card.variant-blue:hover {
        border-color: #3b82f6;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.25);
        transform: translateY(-2px);
    }
    .glass-card.variant-green:hover {
        border-color: #22c55e;
        box-shadow: 0 0 25px rgba(34, 197, 94, 0.25);
        transform: translateY(-2px);
    }
    .glass-card.variant-pink:hover {
        border-color: #ec4899;
        box-shadow: 0 0 25px rgba(236, 72, 153, 0.25);
        transform: translateY(-2px);
    }
    .glass-card.variant-purple:hover {
        border-color: #a855f7;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.25);
        transform: translateY(-2px);
    }

    /* Metric Card Animation & Styling */
    .metric-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .metric-container:hover {
        transform: translateY(-3px);
        border-color: rgba(99, 102, 241, 0.4);
    }
    
    /* Button Customization */
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.25s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

API_URL = "http://localhost:8000"

# --- Sidebar with Lottie Animation ---
with st.sidebar:
    if lottie_task:
        st_lottie(lottie_task, height=180, key="task_anim")
    
    st.markdown("### ⚡ System Status")
    try:
        health_res = requests.get(f"{API_URL}/health", timeout=1.5)
        if health_res.status_code == 200:
            st.success("API Gateway: Online")
            api_active = True
        else:
            st.error("API Gateway: Degraded")
            api_active = False
    except:
        st.error("API Gateway: Offline")
        api_active = False
        
    st.markdown("---")
    st.markdown("<p style='color: #6b7280; font-size: 0.85rem; text-align: center;'>Built with FastAPI & Streamlit</p>", unsafe_allow_html=True)

# --- Helper Functions ---
def fetch_tasks():
    try:
        res = requests.get(f"{API_URL}/tasks")
        return res.json() if res.status_code == 200 else []
    except:
        return []

# --- Main App Title & Header ---
st.markdown(
    """
    <div style='margin-bottom: 25px;'>
        <h1 style='font-weight: 800; letter-spacing: -1px; margin-bottom: 5px; background: linear-gradient(90deg, #f3f4f6, #9ca3af); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>⚡ Elite Task Control Center</h1>
        <p style='color: #9ca3af; font-size: 1.05rem;'>High-performance asynchronous workflow orchestration dashboard.</p>
    </div>
    """,
    unsafe_allow_html=True
)

if not api_active:
    st.warning("⚠️ FastAPI backend is unreachable. Run `uvicorn main:app --reload` to activate endpoints.")
    st.stop()

tasks = fetch_tasks()

# --- Metrics Overview ---
total = len(tasks)
completed = sum(1 for t in tasks if t["done"])
pending = total - completed

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="metric-container">
            <p style="color: #9ca3af; margin:0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;">Total Tasks</p>
            <h2 style="margin:6px 0 0 0; font-weight: 700; color: #f3f4f6;">{total}</h2>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="metric-container">
            <p style="color: #9ca3af; margin:0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;">Completed</p>
            <h2 style="margin:6px 0 0 0; font-weight: 700; color: #10b981;">{completed}</h2>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="metric-container">
            <p style="color: #9ca3af; margin:0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;">Pending</p>
            <h2 style="margin:6px 0 0 0; font-weight: 700; color: #f59e0b;">{pending}</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Create Task Glass Container ---
with st.container():
    st.markdown('<div class="glass-card" style="border-color: rgba(99, 102, 241, 0.2);">', unsafe_allow_html=True)
    st.markdown("### ➕ Initialize New Task Pipeline")
    with st.form("create_form", clear_on_submit=True):
        col_input, col_btn = st.columns([4, 1])
        with col_input:
            new_title = st.text_input("Task Title Input", placeholder="Enter task specification...", label_visibility="collapsed")
        with col_btn:
            submitted = st.form_submit_button("Deploy", use_container_width=True)
            
        if submitted:
            if not new_title.strip():
                st.warning("Task description cannot be null.")
            else:
                resp = requests.post(f"{API_URL}/tasks", json={"title": new_title})
                if resp.status_code == 201:
                    st.success("Pipeline updated successfully.")
                    st.rerun()
                else:
                    st.error("Endpoint transaction failed.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Task Stream Grid with 6 Color Variants ---
st.markdown("### 🗂️ Active Task Stream")

if not tasks:
    st.info("No active logs available in repository.")
else:
    # Define the 6 color configurations (Class Name, Dot Accent Hex Code)
    color_variants = [
        ("variant-red", "#ef4444"),       # Red
        ("variant-amber", "#f59e0b"),     # Amber
        ("variant-blue", "#3b82f6"),      # Blue
        ("variant-green", "#22c55e"),     # Forest Green
        ("variant-pink", "#ec4899"),      # Dark Pink
        ("variant-purple", "#a855f7")     # Purple
    ]

    for index, task in enumerate(tasks):
        # Cycle through the 6 options based on index
        variant_class, accent_color = color_variants[index % len(color_variants)]
        
        st.markdown(f'<div class="glass-card {variant_class}">', unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns([0.08, 0.52, 0.2, 0.2])
        
        with c1:
            is_done = st.checkbox("", value=task["done"], key=f"chk_{task['id']}", label_visibility="collapsed")
            
        with c2:
            if is_done != task["done"]:
                requests.put(f"{API_URL}/tasks/{task['id']}", json={"title": task["title"], "done": is_done})
                st.rerun()
                
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="height: 8px; width: 8px; background-color: {accent_color}; border-radius: 50%; display: inline-block;"></span>
                    {'<span style="color: #6b7280; text-decoration: line-through;">' + task['title'] + '</span>' if task['done'] else '<span style="font-weight: 500; color: #f3f4f6;">' + task['title'] + '</span>'}
                </div>
            """, unsafe_allow_html=True)
                
        with c3:
            if st.button("✏️ Modify", key=f"edit_toggle_{task['id']}", use_container_width=True):
                st.session_state[f"edit_mode_{task['id']}"] = not st.session_state.get(f"edit_mode_{task['id']}", False)
                
        with c4:
            if st.button("🗑️ Purge", key=f"del_{task['id']}", use_container_width=True):
                del_res = requests.delete(f"{API_URL}/tasks/{task['id']}")
                if del_res.status_code == 204:
                    st.rerun()
                else:
                    st.error("Purge failure.")
                    
        # Inline Drawer Form
        if st.session_state.get(f"edit_mode_{task['id']}", False):
            st.markdown("<hr style='border-color: rgba(255,255,255,0.06); margin: 12px 0;'>", unsafe_allow_html=True)
            with st.form(key=f"update_form_{task['id']}"):
                up_title = st.text_input("Modify Title", value=task["title"])
                up_status = st.checkbox("Mark Completed", value=task["done"])
                if st.form_submit_button("Commit Changes"):
                    up_res = requests.put(f"{API_URL}/tasks/{task['id']}", json={"title": up_title, "done": up_status})
                    if up_res.status_code == 200:
                        st.session_state[f"edit_mode_{task['id']}"] = False
                        st.rerun()
                    else:
                        st.error("Commit failed.")

        st.markdown('</div>', unsafe_allow_html=True)