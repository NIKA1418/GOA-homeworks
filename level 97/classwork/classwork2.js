const emails = [
  "alex.morgan92@example.com",
  "sophie_williams07@testmail.com",
  "daniel.lee88@webmail.net",
  "chris.johnson54@myinbox.org",
  "emma.jackson23@mailbox.co",
  "ryan_taylor77@fastmail.io",
  "natalie.green11@postmail.net",
  "michael.brown45@inboxhub.com",
  "olivia.smith29@cloudmail.org",
  "james_wilson63@netmail.co"
];

const usernames = emails.map(email => email.split("@")[0]);

console.log(usernames);