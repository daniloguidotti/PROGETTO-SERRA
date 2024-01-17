<html>
<!DOCTYPE html>
<?php
echo '<form  method = "POST" action = "dati_post.php">
<table border="1">
    <tr>
        <td>
            <label for="nome">Nome:</label></td><td><input type="text" name="nome" id="nome" required>
        </td>
    </tr>

    <tr>
        <td>
            <label for="cognome">Cognome:</label></td><td><input type ="text" name="cognome" name="cognome" required>
        </td>
    </tr>
    <tr>
    <td>
        <label for="nick">Nickname:</label></td><td><input type="text" name="nick" id="nick" required pattern="^[A-Za-z0-9]+([A-Za-z0-9]*|[._-]?[A-Za-z0-9]+)*$
        ">
    </td>
</tr>
    <tr>
    <td>
        <label for="email">Email:</label></td><td><input type ="Email" name="email" name="email" required pattern="^[\w]{1,}[\w.+-]{0,}@[\w-]{2,}([.][a-zA-Z]{2,}|[.][\w-]{2,}[.][a-zA-Z]{2,})$" title="Formato non valido">
    </td>
</tr>
<tr>
<td>
    <label for="data">Data Di Nascita:</label></td><td><input type ="date" name="data" name="data" required>
</td>

</tr>
    <tr>
      <td>
       <label for ="password">Password:</label></td> <td><input type="password"  id="password" name="password" required pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Deve contenere almeno un numero, una lettera maiuscola, una lettera minuscola, e almeno 8 o più caratteri">
    </td> 
</tr>
<tr>
<td>
<a href="Paginaaccesso.php">Hai gia un account? Accedi</a>
</td>
    <td>
<input type="submit" name="invia" id="invia" value="Submit">
<input type="reset" name="invia" id="invia" value="Reset">
</td>
</tr> </form>'
?>
</html>