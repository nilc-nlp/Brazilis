<?php 
require('texts/projects/brazilis/srl/index.php');
require('includes/projects/brazilis/srl/src/tmp.php');  
?>

<div class="masthead">
    <a style="text-decoration:None;" href="index.php"><h1 class="text-muted"><?php echo $title; ?></h1></a>

    <div class="bs-example bs-example-tabs">
    <ul id="myTab" class="nav nav-tabs" style="margin-bottom:5px;">
            <li rel="tooltip" title="<?php echo $tooltip_menu_ferramenta;?>" class="active"><a href="#ferramenta" data-toggle="tab"><?php echo $ferramenta; ?></a></li>
            <li rel="tooltip" title="<?php echo $tooltip_menu_sobre;?>" class=""><a href="#sobre" data-toggle="tab"><?php echo $sobre; ?></a></li>
        </ul>
        <div id="myTabContent" class="tab-content">
            <div class="tab-pane fade" id="sobre">
		<br/>
                <?php echo $introducao1; ?>
                <?php echo $introducao2; ?>


		<div class="page-header">
			<h3><?php echo $referencias;?></h3>
		</div>
            </div>
            <div class="tab-pane fade active in" id="ferramenta">
                    <div class="well">
                        <div class="list-group-item">
                            <span class="label label-default"><?php echo $input_sentence; ?></span><textarea id='input_sentence' placeholder="<?php echo $input_sentence_default;?>" name="sentence" class="form-control" rows=3></textarea>
                            <div class="row">
                                <div class="text-center">

                                    <br/>
                                    <div id="submit-simple">
                                        <button id="button_normalizar" class="btn btn-default" onclick="srl.call_python('button_normalizar');"><?php echo $normalize;?></button>
                                    </div>

                                </div>
                            </div>

                            <span class="label label-success"><?php echo $normalized_sentence;?></span>
                            <div contenteditable="false" id="output_sentence" class="form-control uneditable-input" rows=3 disabled style="background-color: white; color:black; height:auto; overflow:visible; min-height:70px;"></div>

                            <div class="text-center">
                                <br/>
                                <button type="button" class="btn btn-default btn-mini" onclick="srl.clean();"><?php echo $clean;?></button>
                            </div>
                        </div>
                    </div>

            </div>

        </div>
    </div>



</div>

