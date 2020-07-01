<?php
/*	include('tmp.php');

	if($_POST){
		$tmp_file = write_tmp_file($_POST['operation'], $_POST['sentence']);
		exec("tokenizer/webtok < ".$tmp_file. " > ".$tmp_file."0");
		exec("python toolkit.py ".$tmp_file."0");

                exec("python iso-utf-file.py ".$tmp_file."01 1");

		$file_handle = fopen($tmp_file."011", "r");
		$corrected_sentence = '';
		while (!feof($file_handle)) {
 		  $line = fgets($file_handle);
 		  $corrected_sentence = $corrected_sentence.$line;
		}
		fclose($file_handle);
		if($_POST['palavras'] == '1'){
			exec("cat ".$tmp_file."01"." | /usr/local/palavras/portpars/runbick.sem > ".$tmp_file."2");

        	        exec("python iso-utf-file.py ".$tmp_file."2 2");
			$file_handle = fopen($tmp_file."22", "r");
			$palavras_output = '';
			while (!feof($file_handle)) {
 			  $line = fgets($file_handle);
 			  $palavras_output = $palavras_output.$line;
			  }
			fclose($file_handle);
			}
		else{
			$output_palavras = '';
		}
		$response['corrected_sentence'] = $corrected_sentence;
		$response['output_palavras'] = $palavras_output;

		exec("rm ".$tmp_file.' '.$tmp_file.'0'.' '.$tmp_file.'01'.' '.$tmp_file.'011'.' '.$tmp_file.'2'.' '.$tmp_file.'22');
		echo(json_encode($response));

	}	
	else echo('Not posting!');
	exit();
*/

	include('tmp.php');

	if($_POST){
		$tmp_file = write_tmp_file($_POST['operation'], $_POST['sentence']);
		exec("tokenizer/webtok < ".$tmp_file. " > ".$tmp_file."0");
		$corrected_sentence = exec("python toolkit.py ".$tmp_file."0");

			exec('perl callPalavras_flat.pl "'.$corrected_sentence.'" '.$tmp_file.'2');
			$file_handle = fopen($tmp_file."2", "r");
			$palavras_output = '';
			while (!feof($file_handle)) {
 			  $line = fgets($file_handle);
 			  $palavras_output = $palavras_output.$line;
			  }
			fclose($file_handle);
	
		$response['corrected_sentence'] = $corrected_sentence;
		$response['output_palavras'] = $palavras_output;

		exec("rm ".$tmp_file.' '.$tmp_file.'0'.' '.$tmp_file.'01'.' '.$tmp_file.'011'.' '.$tmp_file.'2');
		echo(json_encode($response));

	}	
	else echo('Not posting!');
	exit();
?>
