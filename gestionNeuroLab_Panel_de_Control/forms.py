from django import forms

class FormularioContacto(forms.Form):
	
	nombreComunica=forms.CharField(label= "Nombre", required=True)
	email=forms.EmailField(label= "email", required=True)
	asunto=forms.CharField()
	mensaje=forms.CharField(label= "Mensaje", widget=forms.Textarea)


'''
	
	{% if "valido" in request.GET %}
	
		<p>Gracias por la informacion, nos comunicaremos a la brevedad</p>
	
	{% endif %}
	
	<form action="" method="POST" style="text-align: center;">
		{% csrf_token %}
		<table style="color: white; margin: 20px auto;">{{formulario_contacto.as_table}}</table>
		
		<p>Nombre:<input type="text" name="nombre"></p>
		<p>Asunto:<input type="text" name="asunto"></p>
		<p>Email:<input type="text" name="email"></p>
		p>Mensaje:<textarea name="mensaje" rows="15" cols="45"></textarea></p>
		<input type="submit" value="Enviar" style="width: 150px">
	</form>

</div>
<p style= "color: yellow;">{{request.POST}}</p>
'''


# esto es de formulario_contacto

'''	<h1>Esperamos tu Contacto</h1>
		
		
	{% if form.errors %}
		<p style= "color: red;">Por favor revisa este campo</p>
	{% endif %}
		
		
		
	<form action="" method="POST"> {% csrf_token %}
		<table>
			{{ form.as_table}}
		</table>
		<input type="submit" value="Enviar">
		
	</form>'''
		
'''<div class="contenedorFormulario">
	<table style="color: white; margin: 20px auto;">{{formulario_contacto.as_table}}</table>
</div>'''
