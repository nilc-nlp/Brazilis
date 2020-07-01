use strict;
use LWP::UserAgent;

my $sentence = $ARGV[0];
my $file = $ARGV[1];

my $ua = new LWP::UserAgent;

#my $IP = "10.11.14.19";
my $IP = "143.107.183.175:20008";

my $response = $ua->post('http://'.$IP.'/WSPalavras_flat.php', 
{ Sent => $sentence,});

my $content = $response->content; 

open(FILE,">".$file);
print FILE $content;
close(FILE);
