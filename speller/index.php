<?php 
require('texts/projects/brazilis/speller/index.php');
require('includes/projects/brazilis/speller/src/tmp.php');  
?>

<div class="masthead">
    <a style="text-decoration:None;" href="index.php"><h1 class="text-muted"><?php echo $title; ?></h1></a>


    <div class="bs-example bs-example-tabs">
    <ul id="myTab" class="nav nav-tabs" style="margin-bottom:5px;">
            <li rel="tooltip" title="<?php echo $tooltip_menu_ferramenta;?>" class="active"><a href="#ferramenta" data-toggle="tab"><?php echo $ferramenta; ?></a></li>
            <li rel="tooltip" title="<?php echo $tooltip_menu_sobre;?>" class=""><a href="#sobre" data-toggle="tab"><?php echo $sobre; ?></a></li>
            <li><a rel="tooltip" title="<?php echo $tooltip_download_dicionarios;?>" style="cursor:pointer;" onclick="window.location='includes/projects/brazilis/speller/dics.tar.gz';"><span class="glyphicon glyphicon-download"></span><span> </span><?php echo $download_lexicos; ?></a></li>
        </ul>
        <div id="myTabContent" class="tab-content">
            <div class="tab-pane fade" id="sobre">
                <?php echo $introducao1; ?>

                <div class='panel panel-primary'>
                    <div class='panel-heading'>
                        <h3 class='panel-title'><?php echo $estatisticas_anotacao; ?></h3>
                    </div>
                    <div class='panel-body'>
                        <table class='table table-striped'>
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th><?php echo $categoria; ?></th>
                                    <th>Tokens</th>
                                    <th><?php echo $abreviacao; ?></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td><?php echo $siglas; ?></td>
                                    <td>172</td>
                                    <td>SI</td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td><?php echo $nomes_proprios; ?></td>
                                    <td>1023</td>
                                    <td>NP</td>
                                </tr>
                                <tr>
                                    <td>3</td>
                                    <td><?php echo $abreviacoes; ?></td>
                                    <td>77</td>
                                    <td>AB</td>
                                </tr>
                                <tr>
                                    <td>4</td>
                                    <td><?php echo $internetes; ?></td>
                                    <td>55</td>
                                    <td>IN</td>
                                </tr>
                                <tr>
                                    <td>5</td>
                                    <td><?php echo $estrangeirismos; ?></td>
                                    <td>265</td>
                                    <td>ES</td>
                                </tr>
                                <tr>
                                    <td>6</td>
                                    <td><?php echo $unidade_medida; ?></td>
                                    <td>12</td>
                                    <td>UM</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                </div>
                <?php echo $introducao2; ?>

            </div>
            <div class="tab-pane fade active in" id="ferramenta">
                <div class="list-group-item">   
                    <div id="panel-simple">

                        <div class="panel">
                            <button rel="tooltip" title="<?php echo $tooltip_normalizacao_simples;?>" type="button" class="btn btn-primary btn-mini" onclick="my_app.switch_simple_advanced('simple');"><?php echo $normalizacao_simples;?></button>
                            <button rel="tooltip" title="<?php echo $tooltip_normalizacao_avancada;?>" type="button" class="btn btn-default btn-mini" onclick="my_app.switch_simple_advanced('advanced');"><?php echo $normalizacao_avancada;?></button>
                        </div>
                    </div>

                    <div id="panel-advanced" style="display:none;">
                        <div class="panel">
                            <button rel="tooltip" title="<?php echo $tooltip_normalizacao_simples;?>" type="button" class="btn btn-default btn-mini" onclick="my_app.switch_simple_advanced('simple');"><?php echo $normalizacao_simples; ?></button>
                            <button rel="tooltip" title="<?php echo $tooltip_normalizacao_avancada;?>" type="button" class="btn btn-primary btn-mini" onclick="my_app.switch_simple_advanced('advanced');"><?php echo $normalizacao_avancada; ?></button>
                        </div>

                        <label class="checkbox" >
                            <input id="button_palavras" type="checkbox" onclick="my_app.show_palavras();" />
                            <span <span rel="tooltip" title="<?php echo $tooltip_palavras;?>"><?php echo $palavras_output;?></span>
                        </label>

                        <label class="checkbox">
                            <input id="button_jobs" type="checkbox"/>
                            <span <span rel="tooltip" title="<?php echo $tooltip_lexicon_sequence; ?>"><?php echo $multiple_jobs;?></span>
                        </label>
                    </div>

                    <div class="well">
                        <div class="list-group-item">
                            <span class="label label-default"><?php echo $input_sentence; ?></span><textarea id='input_sentence' placeholder="<?php echo $input_sentence_default;?>" name="sentence" class="form-control" rows=3></textarea>
                            <div class="row">
                                <div class="text-center">

                                    <br/>
                                    <div id="submit-simple">
                                        <button id="button_normalizar" class="btn btn-default" onclick="my_app.call_python('si np ab in es um as', 'button_normalizar');"><?php echo $normalize;?></button>
                                    </div>

                                    <div id="submit-advanced" style="display:none;">
                                        <button id="button_sigla" class="btn btn-default" onclick="my_app.call_python('si', 'button_sigla');"><?php echo $sigla; ?></button>
                                        <button id="button_nome_proprio" class="btn btn-default" onclick="my_app.call_python('np', 'button_nome_proprio');"><?php echo $nome_proprio; ?></button>
                                        <button id="button_abreviacao" class="btn btn-default" onclick="my_app.call_python('ab', 'button_abreviacao');"><?php echo $abreviacao; ?></button>
                                        <button id="button_internetes" class="btn btn-default" onclick="my_app.call_python('in', 'button_internetes');"><?php echo $internetes; ?></button>
                                        <button id="button_estrangeirismo" class="btn btn-default" onclick="my_app.call_python('es', 'button_estrangeirismo');"><?php echo $estrangeirismo; ?></button>
                                        <button id="button_unidade_medida" class="btn btn-default" onclick="my_app.call_python('um', 'button_unidade_medida');"><?php echo $unidade_medida; ?></button>
                                        <button id="button_aspell" class="btn btn-default" onclick="my_app.call_python('as', 'button_aspell');">Aspell</button>
                                    </div>
                                    <!--<img src="includes/projects/brazilis/speller/dist/fonts/down_arrow.png"/>!-->
                                </div>
                            </div>

                            <span class="label label-success"><?php echo $normalized_sentence;?></span>
                            <!--<textarea id="output_sentence" class="form-control uneditable-input" rows=3 disabled style="background-color: white;"></textarea>!-->
                            <div contenteditable="false" id="output_sentence" class="form-control uneditable-input" rows=3 disabled style="background-color: white; color:black; height:auto; overflow:visible; min-height:70px;"></div>

                            <div id="div_output_palavras" style="display:none;">
                                <br/>
                                <span class="label label-info"><?php echo $palavras_output; ?></span>
                                <textarea id="output_palavras" class="form-control" rows=3></textarea>
                                <br/>
                            </div>

                            <div class="text-center">
                                <br/>
                                <button type="button" class="btn btn-default btn-mini" onclick="my_app.clean();"><?php echo $clean;?></button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>



</div>

