<html>
<script>
function add(){
var num1=document.form.text1.value;
var num2=document.form.text2.value;
var sum=Number(num1)+Number(num2);
alert("Sum of two numbers is: "+sum);
}
function divide(){
var num1=document.form.text1.value;
var num2=document.form.text2.value;
var sum=Number(num1)/Number(num2);
alert("Result is: "+sum);
}
function product(){
var num1=document.form.text1.value;
var num2=document.form.text2.value;
var sum=Number(num1)*Number(num2);
alert("Product is: "+sum);
}
function modulus(){
var num1=document.form.text1.value;
var num2=document.form.text2.value;
var sum=Number(num1)%Number(num2);
alert("Modulus is: "+sum);
}
</script>
<form name="form">
<table>
<tr>
<td>Enter First Number:</td>
<td><input type="text" name="text1"></td>
</tr>
<tr>
<td>Enter Second Number:</td>
<td><input type="text" name="text2"></td>
</tr>
<tr>
<td><input type="button" value="Add" onclick="add();"></td>
<td><input type="button" value="Divide" onclick="divide();"></td>
</tr>
<tr>
<td><input type="button" value="Product" onclick="product();"></td>
<td><input type="button" value="Modulus" onclick="modulus();"></td>
</tr>
</table>
</html>
