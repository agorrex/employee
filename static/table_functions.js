
    function removeFromArray(arr, item){
            var index = arr.indexOf(parseInt(item,10));
            if (index > -1) {
              arr.splice(index, 1);
            }
    }

    function addToArray(arr, item){
           if(checkIfIdExists(arr, item)){
                arr.push(parseInt(item,10));
           }
           arr.sort();
    }

    function checkIfIdExists(arr, item){
            var index = arr.indexOf(parseInt(item,10));
//            console.log(item);
//            console.log(index);
            if (index > -1) {
              return false;
            }else if(item == ''){
              return false;
            }else{
              return true;
            }
    }

    function makeIdList(array ,rowData, choice){

       if(choice === 'select'){
           var item = rowData[0][2];
           addToArray(array, item);
       }else if(choice === 'select_all'){
            rowData.forEach(function(currentValue, index, arr){
                addToArray(array, currentValue[2]);
            });
       }else if(choice === 'remove'){

        rowData.forEach(function(currentValue, index, arr){
                removeFromArray(array, currentValue[2]);
            });

       }
       hideOrShowButton(array);
//       console.log(array);
    }

    function hideOrShowButton(array){
        if(checkIfArrayEmpty(array)){
            showButton();
        }else{
            hideButton();
        }

    }

    function checkIfArrayEmpty(array){

        if (typeof array !== 'undefined' && array.length > 0) {
                return true;
        }else{
                return false;
        }
    }


    function hideButton(){
        $("#delete_button").hide();
        $("#export_button").hide();
    }

    function showButton(){
        $("#delete_button").show();
        $("#export_button").show();
    }

    function deleteSelectedObjects(url, list_ids){
            if(checkIfArrayEmpty(list_ids) && confirm('Do you want to delete ?')){
                var saveData = $.ajax({
                  'url': url,
                  'type': 'POST',
                  'data': JSON.stringify({"id_list": list_ids}),
                  'headers': {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        },
                  'dataType': "json",
                  'success': function(resultData) { location.reload(); }
                            });
                saveData.error(function() { alert("Something went wrong"); });
                }
    }

    function exportSelectedObjects(url, list_ids){
        if(checkIfArrayEmpty(list_ids)){
            var load_location = url + '?id_list=' + list_ids.join() ;
            window.open(load_location, '_blank');
        }

    }

