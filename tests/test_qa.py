def test_qa(desktop_app):
    desktop_app.check_page_start()
    desktop_app.give_now_button()
    desktop_app.secure_donation()
    desktop_app.check_cover_transaction_costs()
    desktop_app.payment_option()
    desktop_app.credit_card()
    desktop_app.personal_information()