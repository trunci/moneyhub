# MoneyHub

##Eduardo Trunci, Lucas Katayama, Davi Nakajima An, Bruno Rigo
##GATech 
##Entry for BRASA Hacks 2020

##API Usage

### This API consists of a list of HTTP request urls that connect the server to the frontend with the required information

1. Get User Information
	- Return type: user (struct)
	- Params: cpf (int)
	- `/fetch_user/<int:cpf>/`

2. Get User Specific Field
	- Return type: any
	- Params: cpf (int), field (string)
	- `/fetch_user_info/<int:cpf>/<field>`

3. Update user Info
	- Return: True
	- Params: cpf (int), field (string), value (string)
	- `/update_user_info/<int:cpf>/<field>/<value>`

4. Store new User
	- Return: String
	- Params: cpf (int), name (string)
	- `/new/<int:cpf>/<name>`

4. Davi
	- Return: Number
	- Params: -
	- `davi`
