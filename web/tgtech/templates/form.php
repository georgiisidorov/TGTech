<?php
  error_reporting(E_ALL);
  ini_set('display_errors', 1);
  if(isset($_POST['submitButton'])){
    $token = "5611284544:AAH6ski3WLZzNRE5P6fx-2pJA7KUtsi7kvk";
    $chat_id = '6690957514';

    // $textErr = $phoneErr = $emailErr = '';


    $text_string = 'Имя: %s';
    $phone_string = 'Телефон: %s';
    $email_string = 'Email: %s';
    $source = 'Откуда: сайт';
    $underscore = '_________________________';

    // $text = $phone = $email = '';

    // if (empty($_POST['username'])) {
    //   $textErr = 'Введите имя';
    // } else {
    $text = sprintf($text_string, $_POST['username']);
    //   $text = test_input($_POST['username']);
    // }

    // if (empty($_POST['phone_number'])) {
    //   $phoneErr = 'Введите номер телефона';
    // } else {
    $phone = sprintf($phone_string, $_POST['phone_number']);
    //   $phone = test_input($_POST['phone_number']);
    // }

    // if (empty($_POST['email'])) {
    //   $emailErr = 'Введите электронную почту';
    // } else {
    $email = sprintf($email_string, $_POST['email']);
    //   $email = test_input($_POST['email']);
    // }

    // function test_input($data) {
    //   $data = trim($data);
    //   $data = stripcslashes($data);
    //   $data = htmlspecialchars($data);
    //   return $data;
    // }

    // if (empty($text)) or (empty($phone)) or (empty($email)) {
      
    // }

    header("Location: https://tg-tech.ru/form.html");
    $response = file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$underscore");
    $response = file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$source");
    $response = file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$text");
    $response = file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$phone");
    $response = file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=$email");
  }
  die;
?>



