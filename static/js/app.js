
//var webHost = "http://127.0.0.1:8000";
var webHost = "http://127.0.0.1:8000";



function switchVisible() {

        if (document.getElementById('Div1')) {

            if (document.getElementById('Div1').style.display == 'none') {
                document.getElementById('Div1').style.display = 'block';
                document.getElementById('Div2').style.display = 'none';
                document.getElementById('edit-subscription-button').innerHTML = '<i class="icon-pencil7"></i> Modifier';
            }
            
            else {
                document.getElementById('Div1').style.display = 'none';
                document.getElementById('Div2').style.display = 'block';
                document.getElementById('edit-subscription-button').innerHTML = '<i class="icon-cross"></i> Annuler';
            }
        }
}


function switchVisibleSuperAdmin() {

        if (document.getElementById('Div1_superAdmin')) {

            if (document.getElementById('Div1_superAdmin').style.display == 'none') {
                document.getElementById('Div1_superAdmin').style.display = 'block';
                document.getElementById('Div2_superAdmin').style.display = 'none';
                document.getElementById('edit-superadmin-button').innerHTML = '<i class="icon-pencil7"></i> Modifier';
            }
            
            else {
                document.getElementById('Div1_superAdmin').style.display = 'none';
                document.getElementById('Div2_superAdmin').style.display = 'block';
                document.getElementById('edit-superadmin-button').innerHTML = '<i class="icon-cross"></i> Annuler';
            }
        }
}

function confirmRemovePupilFromClass(classe_id,pupil_id){
     
        swal({
            title: "Êtes-vous sûr de vouloir supprimer l'élève?",
            text: "Cet élève ne fera plus partie de cette classe!",
            type: "warning",
            showCancelButton: true,
            cancelButtonText: "Annuler",
            confirmButtonColor: "#FF7043",
            confirmButtonText: "Oui, supprimer!"
        },
            function(isConfirm){
                if(isConfirm) 
                {
                    //swal("Supprimé","l'élève a été supprimé","success")
                    window.location=window.webHost+'/school/class/'+classe_id+'/pupil/'+pupil_id+'/remove';
                }
            });
        
    
}


/**********  START Add teacher to class   ***********/





function confirmRemoveParentFromPupil(pupil_id,parent_id){
     
        swal({
            title: "Êtes-vous sûr de vouloir supprimer Le parent d'élève?",
            text: "Ce Parent ne fera plus partie de ce élève!",
            type: "warning",
            showCancelButton: true,
            cancelButtonText: "Annuler",
            confirmButtonColor: "#FF7043",
            confirmButtonText: "Oui, supprimer!"
        },
            function(isConfirm){
                if(isConfirm) 
                {
                    //swal("Supprimé","l'élève a été supprimé","success")
                    window.location=window.webHost+'/school/pupil/'+pupil_id+'/parent/'+parent_id+'/remove';
                }
            });
          
}

$(function(){
    $("#search").keyup( function() {
        $("#search-results-default-father").remove();
        $.ajax({ 
           //url: window.webHost+'/school/class/'+classe_id+'/'+subject_id+'/'+teacher_id+'/add-teacher-to-subject',*/
            type: "POST",
            url:window.webHost+'/school/search/father',

            data:{
                'search_text':$('#search').val(),
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType:'html'

        });
    }); 

     $("#search_mother").keyup( function() {
        $("#search-results-default-mother").remove();
        $.ajax({ 
            type: "POST",
            url:window.webHost+'/school/search/mother',
            data:{
                'search_text_mother':$('#search_mother').val(),
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessMother,
            dataType:'html'

        });
    }); 

});

function searchSuccess(data,textStatus,jqXHR)
{ //alert('hopeee');
    $('#search-results').html(data);
}

function searchSuccessMother(data,textStatus,jqXHR)
{ //alert('hopeee');
    $('#search-results-mother').html(data);
}

/* Function to limit the number of checkbox selcted items*/
function limit3(ele,classSet){
    var chks = document.getElementsByClassName(classSet);
    var disallow = 2;//+1 from allowed, so counting down results in 0 @ more than allowed
    for(var i = chks.length>>>0; i--;){
        if(chks[i].checked) disallow--;
        if(!disallow){
            ele.checked = false;
            break;
        }
    }
}





function getClasses(level_id){
 $.ajax({  
        url: window.webHost+'/school/level/'+level_id+'/display/classes',
        //url:window.webHost+'/school/display/classes/',
        success:  function(data) {
        //alert( window.webHost+'/school/level/1/display/classes/');
        //alert(data);
        $('#slideBarClasses').html(data);
        //alert('i am here');
        },
        dataType:'html'

    });
}




$(function(){
    $('input.single-checkbox').change(function(e){
       if ($('input[type=checkbox]:checked').length > 1) {
            $(this).prop('checked', false)
            alert("allowed only 3");
       }
    });
});

$('input[type=checkbox]').on('change', function (e) {
    if ($('input[type=checkbox]:checked').length > 1) {
        $(this).prop('checked', false);
        alert("allowed only 3");
    }
});


