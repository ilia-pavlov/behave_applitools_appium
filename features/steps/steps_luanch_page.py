from behave import given, when, then


@given('tap on Get started button on launch page')
def tap_get_started(context):
    context.app.launch_screen.tap_get_started()


@then('Tap on info button')
def tap_info_button(context):
    context.app.launch_screen.tap_info_icon()


@then('tap on Cancel cta')
def tap_cancel_cta(context):
    context.app.launch_screen.tap_cancel_cta()


@then('observe {title} screen')
def observe_welcome_screen(context, title):
    context.app.launch_screen.assert_welcome_screen(title)

'''
@given('tap on login cta on launch page')
def tap_login_cta(context):
    context.app.launch_screen.tap_login_cta()

@when('Input {valid_email_dev} to email field')
def input_valid_email_dev(context, valid_email_dev):
    context.app.login_screen.input_email(valid_email_dev)


@then('Input {valid_password} to password field')
def input_valid_password(context, valid_password):
    context.app.login_screen.input_password(valid_password)


@then('Tap on login button')
def tap_login_button(context):
    context.app.login_screen.tap_login_button()


@then('Home dashboard is opened, {title} displays')
def verify_login_state(context, title):
    context.app.home_dashboard.verify_login_state(title)
'''
