public class LoginController implements OnClickListener{
	private LoginView loginView;
	private LoginControllerListener listener;
	public LoginController(LoginView loginView, LoginControllerListener listener) {
		this.loginView = loginView;
		this.listener = listener;
	}

	/** Login button was clicked */
	@Override
	public void onClick(View v) {
		// Check for a valid email address.
		if(loginView.getLogin().isEmpty() || loginView.getLogin().equals(""))
			loginView.setLoginError(ErrorConstants.ERROR_FIELD_REQUIRED);
		else
			if(!loginView.getLogin().contains("@"))
				loginView.setLoginError(ErrorConstants.ERROR_INVALID_EMAIL);

		// Check for a valid password.
		if(loginView.getPassword().isEmpty() || loginView.getPassword().equals(""))
			loginView.setPasswordError(ErrorConstants.ERROR_FIELD_REQUIRED);
		else
			if(loginView.getPassword().length() < 3)
				loginView.setPasswordError(ErrorConstants.ERROR_INVALID_PASSWORD);
		else {
			//If all inputs are rights than go next and call a web service that will verify the login. Use Model to map inputs
            LoginRequest requestObject = new LoginRequest(username, password);
            Boolean result = requestObject.attemptLogin();
            if (result)
			    listener.onLoginSuccess();
        }
	}

}