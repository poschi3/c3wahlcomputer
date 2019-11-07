<?php

$name = "c3account";
$value = uniqid("", true);
$expire = time() + (10 * 365 * 24 * 60 * 60);

setcookie($name, $value, $expire, '/');

?>
