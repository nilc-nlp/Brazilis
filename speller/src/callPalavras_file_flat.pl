use strict;
use LWP::UserAgent;

my $fileIn = $ARGV[0];
my $fileOut = $ARGV[1];
my $ua = new LWP::UserAgent;

#my $IP = "10.11.14.19";
my $IP = "143.107.183.175:20008";

my $response = $ua->post
	(
		'http://'.$IP.'/WSPalavras_file_flat.php', 
		Content_Type => 'form-data', 
		Content => 
		[ 
			Files => [ $fileIn ],
		]
	);
	
my $content = $response->content; 

open(FILE,">".$fileOut);
print FILE $content;
close(FILE);
