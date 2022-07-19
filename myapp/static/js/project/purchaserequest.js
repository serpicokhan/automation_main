
$(function () {


  var loadForm =function (btn1) {
    var btn=0;
    //console.log(btn1);
    if($(btn1).attr("type")=="click")
     btn=$(this);
    else {
      btn=btn1;
    }
    //console.log($(btn).attr("type"));
    //console.log($(btn).attr("data-url"));
    return $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        // $("#modal-purchaseRequest").html('');

        $("#modal-purchaseRequest").modal({backdrop: 'static', keyboard: false});
      },
      success: function (data) {

        $("#modal-purchaseRequest .modal-content").html(data.html_purchaseRequest_form);
        $('.selectpicker').selectpicker();


        $('.advanced2AutoComplete').autoComplete({
          resolver: 'custom',
          minChars:1,
          formatResult: function (item) {
            return {
              value: item.id,
              text: "[" + item.partCode + "] " + item.partName,

            };
          },
          events: {
            search: function (qry, callback) {
              // let's do a custom ajax call
              $.ajax(
                '/Part/Get/',
                {
                  data: { 'qry': qry}
                }
              ).done(function (res) {
                callback(res)
              });
            },

          }
        });
        $('.advanced2AutoComplete').on('autocomplete.select', function (evt, item) {
          $("#id_PurchaseRequestPartName").val(item.id);
          $('#id_PurchaseRequestPartName').val(item.id).trigger('change');
          // $('.basicAutoCompleteCustom').html('');
        });
        if($("#id_PurchaseRequestDateTo").val().length>0)
          $("#id_PurchaseRequestDateTo").pDatepicker({
            format: 'YYYY-MM-DD',
            initialValueType: 'gregorian',
            autoClose:true
          });
        else{
          $("#id_PurchaseRequestDateTo").pDatepicker({
            format: 'YYYY-MM-DD',

            autoClose:true
          }).val('');

        }
        if($("#id_PurchaseRequestDateFrom").val().length>0)
          $("#id_PurchaseRequestDateFrom").pDatepicker({
            format: 'YYYY-MM-DD',
            initialValueType: 'gregorian',
            autoClose:true
          });
          else {
            $("#id_PurchaseRequestDateFrom").pDatepicker({
              format: 'YYYY-MM-DD',

              autoClose:true
            }).val('');
          }





      }
    });



};
var cancelForm=function(){

  $.ajax({
    url: '/PurchaseRequest/'+$("#lastPurchaseRequestid").val()+'/Cancel/',

    type: 'get',
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        //alert("taskGroup created!");  // <-- This is just a placeholder for now for testing

        $("#tbody_purchaseRequest").empty();
        $("#tbody_purchaseRequest").html(data.html_purchaseRequest_list);


        // $("#modal-taskGroup").modal("hide");
       // console.log(data.html_taskGroup_list);
      }
      else {

        // $("#purchaseRequest-table tbody").html(data.html_part_list);
        // $("#modal-purchaseRequest .modal-content").html(data.html_part_form);
      }
    }
  });
  return false;


};
var ids=[];
var tbl_purchase_content="";
//$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-create-form",
var saveForm= function () {
    // alert("!23");
   var form = $(this);
   var tbody=$("#tbody_purchaseRequest");
   var part_name=$("#id_mypart").val();
   var part_qty=$("#id_PurchaseRequestAssetQty").val();
   var tajhiz=$( "#id_PurchaseRequestAsset option:selected" ).text();



   $.ajax({
     url: form.attr("action"),
     data: form.serialize(),
     type: form.attr("method"),
     dataType: 'json',
     error:function(x,y,z){
       console.log(x.responseText);
       alert("error");
     },
     beforeSend:function(xhr){
       if($("#id_PurchaseRequestPartName").val()==0)
       {
         toastr.error("نام قطعه معتبر نیست","",{positionClass: "toast-top-full-width",});
         xhr.abort();
       }
     },
     success: function (data) {
       if (data.form_is_valid) {
         //alert("Company created!");  // <-- This is just a placeholder for now for testing
         $("#tbody_purchaseRequest").empty();
         var row=`<tr><td></td><td>${part_name}</td><td>${part_qty}</td><td>${tajhiz}</td><td></td><td> <div class="d-flex">
              <a href="#" class="btn btn-primary shadow btn-xs sharp mr-1 btn-sm js-update-purchaseRequest"   data-url="{% url 'purchaseRequest_update' ${data.id} %}"><i class="fa fa-pencil"></i></a>
              <a href="#" class="btn btn-danger shadow btn-xs sharp js-delete-purchaseRequest"  data-url="{% url 'purchaseRequest_delete' ${data.id} %}"><i class="fa fa-trash"></i></a>
          </div></td></tr>`;

         tbl_purchase_content+=row;
         $("#tbody_purchaseRequest").append(tbl_purchase_content);

         ids.push(data.id);
         $("#lastPurchaseRequestid").val(ids);
         // $("#tbody_purchaseRequest").html(data.result);

         $("#modal-purchaseRequest").modal("hide");
        toastr.success("درخواست با موفقیت ذخیره شد","",{ positionClass: "toast-top-full-width"});
       }
       else {


       }
     }
   });
   return false;
 };


 var initPurchaseRequestStockLoad=function(){


   $.ajax({

     url: '/PurchaseRequestStock/'+$("#lastPurchaseRequestid").val()+'/listPurchaseRequestStock',



     success: function (data) {
         //alert($("#lastWorkOrderid").val());
       if (data.form_is_valid) {

         $("#tbody_purchaseRequestStock").empty();
         $("#tbody_purchaseRequestStock").html(data.html_purchaseRequestStock_list);
         $("#modal-purchaseRequestStock").modal("hide");

       }
       else {

         $("#purchaseRequestStock-table tbody").html(data.html_purchaseRequestStock_list);
         $("#modal-purchaseRequestStock .modal-content").html(data.html_purchaseRequestStock_form);
       }
     }
   });
return false;
 };



 var myprLoader= function(){
   btn=$(this);
   // console.log("1");




   //$.when(loadForm(btn)).done(initLoad,initWoPurchaseRequestLoad,initWoMeterLoad,initWoMiscLoad,initWoNotifyLoad,initWoFileLoad);
   // $.when(loadForm(btn)).done(initPurchaseRequestFileLoad,initPurchaseRequestAssetLoad,initPurchaseRequestPartLoad );
   loadForm(btn);

   //initLoad();
 }
var loadRelatedAsset=function(){
  asset_id=$("#id_PurchaseRequestAssetMakan").val();
  if(asset_id)
  {
    $.ajax({

      url: '/Asset/'+asset_id+'/listRelatedAsset',
      error:function(x,y,z){
        // console.log(x,y,z)

      },


      success: function (data) {
          //alert($("#lastWorkOrderid").val());
        if (data.form_is_valid) {

          $("#id_PurchaseRequestAsset").empty();
          $("#id_PurchaseRequestAsset").html(data.pval);

          // $("#id_PurchaseRequestAsset").selectpicker();
            $('#id_PurchaseRequestAsset').selectpicker('refresh');

        }
        else {


        }
      }
    });
 return false;
  };

}
var filter=function(){
  // alert("!23");
  window.location.replace("/PurchaseRequest/filter/"+"?q="+$("#p-status").val());
}
var loadRelatedAsset=function(){
  asset_id=$("#id_PurchaseRequestAssetMakan").val();
  if(asset_id)
  {
    $.ajax({

      url: '/Asset/'+asset_id+'/listRelatedAsset',
      error:function(x,y,z){
        // console.log(x,y,z)

      },


      success: function (data) {
          //alert($("#lastWorkOrderid").val());
        if (data.form_is_valid) {

          $("#id_PurchaseRequestAsset").empty();
          $("#id_PurchaseRequestAsset").html(data.pval);

          // $("#id_PurchaseRequestAsset").selectpicker();
            $('#id_PurchaseRequestAsset').selectpicker('refresh');

        }
        else {


        }
      }
    });
 return false;
  };

}

$('#modal-purchaseRequest').on('keyup', function (event) {

  var keycode = (event.keyCode ? event.keyCode : event.which);
  if(keycode == '13'){
    alert("AFTER ENTER clicked");
    // $('#getDataBt').click();
  }
});
$("#p-status").on("change",filter);
$(".js-create-purchaseRequest").click(myprLoader);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-create-form", saveForm);

// Update book
$("#purchaseRequest-table").on("click", ".js-update-purchaseRequest", myprLoader);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-update-form", saveForm);
$("#modal-purchaseRequest").on("change", "#id_PurchaseRequestAssetMakan",loadRelatedAsset);
// Delete book
$("#purchaseRequest-table").on("click", ".js-delete-purchaseRequest", loadForm);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-delete-form", saveForm);
$("#modal-purchaseRequest").on("change", "#id_PurchaseRequestAssetMakan",loadRelatedAsset);
// $('#modal-purchaseRequest').on('hidden.bs.modal',cancelForm);
//$("#purchaseRequest-table").on("click", ".js-update-wo", initxLoad);
});
