import streamlit as st
from db_handler import (
    save_or_update_employee,
    export_to_excel
)
ADMIN_PASSWORD = "tcadmin789"
st.set_page_config(
    page_title="TC Skill Evaluation",
    layout="wide"
)
hide_streamlit_style = """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
"""

st.markdown(
    hide_streamlit_style,
    unsafe_allow_html=True
)
# ---------------------------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------------------------

if "step" not in st.session_state:
    st.session_state.step = 1

if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# ---------------------------------------------------
# COMMON DATA
# ---------------------------------------------------

RATING_OPTIONS = ["1", "2", "3", "N/A"]

# ---------------------------------------------------
# STEP NAVIGATION FUNCTIONS
# ---------------------------------------------------

def next_step():
    st.session_state.step += 1


def prev_step():
    st.session_state.step -= 1

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("TC Skill Evaluation Portal")

# ---------------------------------------------------
# STEP 1 — EMPLOYEE DETAILS
# ---------------------------------------------------

if st.session_state.step == 1:

    st.header("Step 1 — Employee Details")

    name = st.text_input(
        "Employee Name",
        value=st.session_state.form_data.get("Name", "")
    )

    cg = st.selectbox(
        "CG",
        ["40", "50", "60", "70"]
    )

    role = st.selectbox(
        "Role",
        [
            "D - Developer",
            "P - Product Owner / Manager",
            "S - Scrum Master",
            "T - Tester",
            "M - Management"
        ]
    )

    if st.button("Next"):

        st.session_state.form_data["Name"] = name
        st.session_state.form_data["CG"] = cg
        st.session_state.form_data["Role"] = role

        next_step()

# ---------------------------------------------------
# STEP 2 — CORE PROGRAMMING SKILLS
# ---------------------------------------------------

elif st.session_state.step == 2:

    st.header("Step 2 — Core Programming Skills")

    skills = {
        "Basic C/C++": "Basic C, C++",
        "Advanced C++": "Advanced C++, C++11/14/17/20",
        "C# Basic": "C# .NET Basic",
        "C# Advanced": "C# .NET Advanced",
        "Threading": "Threading",
        "SW Tools": "SW Tools (Perf/Debugging/Testing)",
        "Win32 API": "Windows Internals / Win32 API"
    }

    for key, label in skills.items():

        st.session_state.form_data[key] = st.radio(
            label,
            RATING_OPTIONS,
            horizontal=True,
            key=key
        )

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:
        st.button("Next", on_click=next_step)

# ---------------------------------------------------
# STEP 3 — UI & COMMUNICATION
# ---------------------------------------------------

elif st.session_state.step == 3:

    st.header("Step 3 — UI & Communication Skills")

    skills = {
        "UI Development":
            "UI Development / REACTJS / MFC / SENSE / WPF / WINFORM",

        "Communication Frameworks":
            "Communication Frameworks (WCF / SSCF)",

        "REST":
            "REST",

        "DICOM":
            "DICOM"
    }

    for key, label in skills.items():

        st.session_state.form_data[key] = st.radio(
            label,
            RATING_OPTIONS,
            horizontal=True,
            key=key
        )

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:
        st.button("Next", on_click=next_step)

# ---------------------------------------------------
# STEP 4 — INTEGRATION & SERVICES
# ---------------------------------------------------

elif st.session_state.step == 4:

    st.header("Step 4 — Integration & Services")

    skills = {
        "Third Party Integration":
            "Third Party Integration",

        "CI/CD":
            "CI/CD / Build Process / Installation",

        "Automation":
            "Automation Practices",

        "Installation Infra":
            "Installation and Infrastructure",

        "Service Platforms":
            "Service Platforms (PSC / IOT / PRS / IST)"
    }

    for key, label in skills.items():

        st.session_state.form_data[key] = st.radio(
            label,
            RATING_OPTIONS,
            horizontal=True,
            key=key
        )

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:
        st.button("Next", on_click=next_step)

# ---------------------------------------------------
# STEP 5 — CLINICAL & WORKFLOW
# ---------------------------------------------------

elif st.session_state.step == 5:

    st.header("Step 5 — Clinical & Workflow")

    skills = {
        "Hospital Workflow":
            "Hospital Workflows",

        "Local Workflow":
            "Local Service Workflow",

        "Remote Workflow":
            "Remote Service Workflow",

        "Clinical Application":
            "Clinical Application (IVUS / Physiology)",

        "Clinical Knowledge":
            "Clinical Application Knowledge",

        "Dev Test Lab":
            "Dev Test Lab Knowledge",

        "Full System Test":
            "Full System Test Knowledge"
    }

    for key, label in skills.items():

        st.session_state.form_data[key] = st.radio(
            label,
            RATING_OPTIONS,
            horizontal=True,
            key=key
        )

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:
        st.button("Next", on_click=next_step)

# ---------------------------------------------------
# STEP 6 — PLATFORM / CLOUD / INFRA
# ---------------------------------------------------

elif st.session_state.step == 6:

    st.header("Step 6 — Platform / Cloud / Infra")

    skills = {
        "Platform":
            "Linux / Windows / Cross Platform",

        "Cloud Native":
            "Containers / Kubernetes / Docker",

        "Cloud":
            "Cloud",

        "AI/ML":
            "AI / ML Basics",

        "Security":
            "Security Basics",

        "GitHub":
            "GitHub",

        "Network Infra":
            "Network Infrastructure",

        "Build Tools":
            "CMake / Conan / Nuget / ISO"
    }

    for key, label in skills.items():

        st.session_state.form_data[key] = st.radio(
            label,
            RATING_OPTIONS,
            horizontal=True,
            key=key
        )

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:
        st.button("Next", on_click=next_step)

# ---------------------------------------------------
# STEP 7 — NOTES & SUBMIT
# ---------------------------------------------------

elif st.session_state.step == 7:

    st.header("Step 7 — Notes & Final Submit")

    note = st.text_area(
        "Additional Notes",
        value=st.session_state.form_data.get("Note", "")
    )

    st.session_state.form_data["Note"] = note

    st.subheader("Rating Scale")

    st.info("""
    1 = Beginner / Foundation  
    2 = Practitioner / Intermediate  
    3 = Expert  
    N/A = Not Applicable
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_step)

    with col2:

        if st.button("Submit Final Evaluation"):

            save_or_update_employee(
                st.session_state.form_data
            )

            st.success("Evaluation Submitted Successfully!")

            st.balloons()

            st.session_state.step = 1
            st.session_state.form_data = {}

# ---------------------------------------------------
# ADMIN SECTION
# ---------------------------------------------------

st.divider()

st.subheader("Admin Access")

admin_password = st.text_input(
    "Enter Admin Password",
    type="password"
)

if admin_password:

    if admin_password == ADMIN_PASSWORD:

        st.success("Admin Access Granted")

        if st.button("Export Database to Excel"):

            file_path = export_to_excel()

            with open(file_path, "rb") as file:

                st.download_button(
                    label="Download Excel Report",
                    data=file,
                    file_name="tc_skill_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    else:

        st.error("Invalid Admin Password")
