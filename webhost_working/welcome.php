<?php 
session_start();
if(!isset($_SESSION["email"])){
	header("location:login.php");
} else {
?>
<html>
<head>
<title>Welcome</title>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel='stylesheet prefetch' href='http://netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css'>
    <link rel="stylesheet" href="style.css">
	<style>
	body{
		text-align:center;
		margin-top: 20px;
	}
	h1.main{
		padding:20px;
		margin-left: 50px;
		margin-right: 50px;
		background-color:grey;
		border-radius: 20px; 
	}
	div.user{
		background-color: skyblue;
		border-radius: 20px;
		margin-left: 50px;
		margin-right: 50px;
	
		padding:20px;
	}
	</style>
</head>
<body>

<button type="button" class="btn btn-bd-green d-none d-lg-inline-block mb-3 mb-md-0 ml-md-3"><a href="logout.php">Logout</a></button>
<h1 class="main">Welcome, <?=$_SESSION['email'];?>!</h1>
<div class="user">
<p>
<h1>This is my first page you see now.</h1>
here you can upload or download your documents.
</p>
<footer>
&copy; suraj Inc.
</footer></div>
</body>
</html>
<?php
}
?>