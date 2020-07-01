<?php 
require('texts/projects/brazilis/subject_insertor/index.php');
require('includes/projects/brazilis/subject_insertor/src/tmp.php');  
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


		<div class="page-header">
			<h3><?php echo $referencias;?></h3>
		</div>
		<div class="list-group">
			<div class="list-group-item">
				<label class="list-group-item-heading" id="hartmannetal2014">Filling the gap: inserting an artificial constituent where a subject is omitted in Portuguese</label>
    				<p class="list-group-item-text">Hartmann, N. S., Duran M. S., Aluísio, S. M. (2014). Filling the gap: inserting an artificial constituent where a subject is omitted in Portuguese. 
Proceedings of I Workshop on Tools and Resources for Automatically Processing Portuguese and Spanish, São Carlos, Brazil.</p> 
			</div>
			<div class="list-group-item">
				<label class="list-group-item-heading" id="palmeretal2005">The proposition bank: An annotated corpus of semantic roles</label>
    				<p class="list-group-item-text">Palmer, M., D. Gildea, and P. Kingsbury (2005). The proposition bank: An annotated corpus of semantic roles. Computational Linguistics 31(1), 71–106.</p> 
			</div>
			<div class="list-group-item">
				<label class="list-group-item-heading" id="toutanovaetal2008"> A global joint model for semantic role labeling</label>
    				<p class="list-group-item-text">Toutanova, K., A. Haghighi, and C. D. Manning (2008). A global joint model for semantic role labeling. Computational Linguistics 34(2), 161–191.</p> 
			</div>
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
                                        <button id="button_normalizar" class="btn btn-default" onclick="subject_insertor.call_python('button_normalizar');"><?php echo $normalize;?></button>
                                    </div>

                                </div>
                            </div>

                            <span class="label label-success"><?php echo $normalized_sentence;?></span>
                            <!--<textarea id="output_sentence" class="form-control uneditable-input" rows=3 disabled style="background-color: white; color:black;"></textarea>!-->
                            <div contenteditable="false" id="output_sentence" class="form-control uneditable-input" rows=3 disabled style="background-color: white; color:black; height:auto; overflow:visible; min-height:70px;"></div>
                            <div class="text-center">
                                <br/>
                                <button type="button" class="btn btn-default btn-mini" onclick="subject_insertor.clean();"><?php echo $clean;?></button>
                            </div>
                        </div>
                    </div>

            </div>

        </div>
    </div>



</div>

