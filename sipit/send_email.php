<?php
// Uključi PHPMailer datoteke
require 'phpmailer/src/PHPMailer.php';  // Glavna PHPMailer klasa
require 'phpmailer/src/Exception.php';  // Klasa za iznimke
require 'phpmailer/src/SMTP.php'; 

// Koristi namespace za PHPMailer
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Provjeri je li forma poslana
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Preuzmi podatke iz forme
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Kreiraj novu instancu PHPMailera
    $mail = new PHPMailer(true);
    
    try {
        // Postavke za SMTP (ako koristiš Gmail)
        $mail->isSMTP(); // Koristi SMTP
        $mail->Host = 'smtp.gmail.com'; // SMTP server za Gmail
        $mail->SMTPAuth = true; // Autentifikacija
        $mail->Username = 'mija.vujnovic2@gmail.com'; // Tvoj Gmail
        $mail->Password = 'wyho ebhm tiqf vtcd'; // Tvoja lozinka ili lozinka aplikacije
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Enkripcija
        $mail->Port = 587; // Port za Gmail SMTP

        // Ko prima email
        $mail->setFrom($email, $name); // Pošiljatelj
        $mail->addAddress('nikicanikica02@gmail.com', 'Nikica Nikica'); // Tvoj email

        // Sadržaj emaila
        $mail->isHTML(true); // Postavi HTML format
        $mail->Subject = 'Nova poruka s kontakt forme';
        $mail->Body    = "<h3>Poruka od: $name</h3><p>Email: $email</p><p>Poruka:</p><p>$message</p>";

        // Pošaljite email
        $mail->send();
        echo 'Poruka je poslana.';
    } catch (Exception $e) {
        echo "Poruka nije poslana. Mailer Error: {$mail->ErrorInfo}";
    }
}
?>