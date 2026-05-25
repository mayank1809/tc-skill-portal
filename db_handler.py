import sqlite3
import pandas as pd
import os

DB_PATH = "data/skill_portal.db"

# ---------------------------------------------------
# CREATE DATABASE + TABLE
# ---------------------------------------------------

def create_database():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (

            Name TEXT,
            CG TEXT,
            Role TEXT,

            "Basic C/C++" TEXT,
            "Advanced C++" TEXT,
            "C# Basic" TEXT,
            "C# Advanced" TEXT,
            "Threading" TEXT,
            "SW Tools" TEXT,
            "Win32 API" TEXT,

            "UI Development" TEXT,
            "Communication Frameworks" TEXT,
            "REST" TEXT,
            "DICOM" TEXT,

            "Third Party Integration" TEXT,
            "CI/CD" TEXT,
            "Automation" TEXT,
            "Installation Infra" TEXT,
            "Service Platforms" TEXT,

            "Hospital Workflow" TEXT,
            "Local Workflow" TEXT,
            "Remote Workflow" TEXT,
            "Clinical Application" TEXT,
            "Clinical Knowledge" TEXT,
            "Dev Test Lab" TEXT,
            "Full System Test" TEXT,

            "Platform" TEXT,
            "Cloud Native" TEXT,
            "Cloud" TEXT,
            "AI/ML" TEXT,
            "Security" TEXT,
            "GitHub" TEXT,
            "Network Infra" TEXT,
            "Build Tools" TEXT,

            Note TEXT
        )
    """)

    conn.commit()
    conn.close()

# ---------------------------------------------------
# INSERT OR UPDATE EMPLOYEE
# ---------------------------------------------------

def save_or_update_employee(data):

    create_database()

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    # CHECK EXISTING EMPLOYEE
    cursor.execute("""
        SELECT rowid
        FROM employees
        WHERE Name = ?
        AND Role = ?
    """, (data["Name"], data["Role"]))

    result = cursor.fetchone()

    # ---------------------------------------------------
    # UPDATE EXISTING
    # ---------------------------------------------------

    if result:

        row_id = result[0]

        columns = []

        values = []

        for key, value in data.items():

            columns.append(f'"{key}" = ?')
            values.append(value)

        values.append(row_id)

        query = f"""
            UPDATE employees
            SET {", ".join(columns)}
            WHERE rowid = ?
        """

        cursor.execute(query, values)

    # ---------------------------------------------------
    # INSERT NEW
    # ---------------------------------------------------

    else:

        columns = ", ".join([f'"{k}"' for k in data.keys()])

        placeholders = ", ".join(["?"] * len(data))

        values = list(data.values())

        query = f"""
            INSERT INTO employees ({columns})
            VALUES ({placeholders})
        """

        cursor.execute(query, values)

    conn.commit()
    conn.close()

# ---------------------------------------------------
# EXPORT TO EXCEL
# ---------------------------------------------------

def export_to_excel():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM employees",
        conn
    )

    export_path = "data/tc_skill_report.xlsx"

    df.to_excel(export_path, index=False)

    conn.close()

    return export_path