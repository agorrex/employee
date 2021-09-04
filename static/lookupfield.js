
// add newly added option to the lookup field
    function addToSelect(selectValues, $select_object, selection){
            var elements = [];
            $.each(selectValues, function(key, value) {
                        elements.push(value);
            });
            $select_object
                 .append($("<option></option>")
                 .attr("value",elements[0])
                 .text(elements[1]))
            elements = []
            console.log(selection);
            $select_object.val(selection);
        }

// show retrieved error message in a alert box in a modal
    function showErrorMessage(response,alertDiv){
       var repMsgObj = response.responseJSON;
       var msg = null;
       $.each(repMsgObj, function(key, value){
                msg = value;
       });
       var alert = alertDiv;
       alert.html(msg);
       alert.show();

    }

    function toJSONString( form ) {
		var obj = {};
		var elements = form.serializeArray();
		for( var i = 0; i < elements.length; ++i ) {
			var element = elements[i];
			var name = element.name;
			var value = element.value;

			if( name ) {
				obj[ name ] = value;
			}
		}
		return JSON.stringify( obj );
	}


    function linkModelToButton(buttonObj){

                        // Code for modal ajax saving and refresing select
                                var modalObjName = buttonObj.attr('data-target');
                                var modalObj = $(modalObjName);
                                var $myForm = modalObj.find("#model-form");
                                var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url

                        // Prevent modal form loading
                                $myForm.on('submit',function(e){
                                e.preventDefault();
                                });


                                modalObj.find("#modal-save").click(function(e){
                                    var $formData = toJSONString($myForm);
                                    console.log($formData);
                                     $.ajax({
                                                method: "POST",
                                                url: $thisURL,
                                                contentType: "application/json; charset=utf-8",
                                                data: $formData,
                                                dataType: "json",
                                                success: handleFormSuccess,
                                                error: handleFormError,
                                            });
                                });

                            function handleFormSuccess(data, textStatus, jqXHR){
                                //console.log(data);
                                //console.log(textStatus);
                                //console.log(jqXHR);
                                $myForm[0].reset();
                                modalObj.modal('toggle');
                                var $selectId = buttonObj.attr('data-select');
                                addToSelect(data,$($selectId), data["id"]);
                                return true;
                            }

                            function handleFormError(jqXHR, textStatus, errorThrown){
                                //console.log(jqXHR);
                                //console.log(textStatus);
                                //console.log(errorThrown);
                                showErrorMessage(jqXHR,modalObj.find('.alert'))
                            }

                        }