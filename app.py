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

        # ---------------------------------------------------
        # EXPORT BUTTON
        # ---------------------------------------------------

        if st.button("Export Database to Excel"):

            file_path = export_to_excel()

            with open(file_path, "rb") as file:

                st.download_button(
                    label="Download Excel Report",
                    data=file,
                    file_name="tc_skill_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        # ---------------------------------------------------
        # CLEAR DATABASE
        # ---------------------------------------------------

        st.divider()

        st.warning(
            "Danger Zone - Admin Only"
        )

        confirm_delete = st.checkbox(
            "I understand this will delete ALL entries"
        )

        if confirm_delete:

            if st.button("Clear All Database Entries"):

                clear_database()

                st.success(
                    "All database entries cleared successfully!"
                )

    else:

        st.error("Invalid Admin Password")
