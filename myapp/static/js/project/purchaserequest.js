
$(function () {

var loadsupplierform=function(){
  // alert("!23");
  return $.ajax({
    url: $(this).attr("data-url"),
    type: 'get',
    dataType: 'json',
    beforeSend: function (x,z) {


      $("#mySupplierModal").modal({backdrop: 'static', keyboard: false});

    },
    success: function (data) {
      // console.log("here!");
      console.log(data);
      $("#mySupplierModal .modal-content").html(data.html_supplier_form);
      // $('.selectpicker').selectpicker();


    }
  });
}
var create_supplier=function(){
  $.ajax({
    url: '/Business/new/?qry='+$("#id_mysupplier").val(),
    type: 'get',
    dataType: 'json',
    success:function(data){
      if(data.is_valid)
      $("id_supplier").val(data.instance);
    }

  });
}
  var loadForm =function (btn1) {
    var btn=0;
    //console.log(btn1);
    if($(btn1).attr("type")=="click")
     btn=$(this);
    else {
      btn=btn1;
    }

    return $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function (x,z) {

        $("#modal-purchaseRequest").modal({backdrop: 'static', keyboard: false});
      },
      success: function (data) {

        $("#modal-purchaseRequest .modal-content").html(data.html_purchaseRequest_form);
        $('.selectpicker').selectpicker();

   //


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
        $('.advanced2AutoComplete2').autoComplete({
          resolver: 'custom',
          minChars:1,
          formatResult: function (item) {
            return {
              value: item.id,
              text: "[" + item.phone + "] " + item.name,

            };
          },
          events: {
            search: function (qry, callback) {
              // let's do a custom ajax call
              $.ajax(
                '/Business/Get/',
                {
                  data: { 'qry': qry}
                }
              ).done(function (res) {
                if(res.length==0){
                  $(".js-create-supplier").show();
                }
                callback(res)
              });
            },

          }
        });
        $('.advanced2AutoComplete2').on('autocomplete.select', function (evt, item) {
          $("#id_supplier").val(item.id);
          $('#id_supplier').val(item.id).trigger('change');
          // $('.basicAutoCompleteCustom').html('');
        });







      }
    });



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
   // var ijade_vaghfe=$("#checkkBoxId").attr("checked")?"<i class="fa fa-close"></i>":"";



   $.ajax({
     url: form.attr("action"),
     data: form.serialize(),
     type: form.attr("method"),
     dataType: 'json',
     error:function(x,y,z){
       // console.log(x.responseText);
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
         if(data.update)
         {
          
           // $("#tbody_purchaseRequest").html(data.result);
           tb=$("#purchaseRequest-table");
           tb.find("tr").each(function(index, element) {
             var colSize = $(element).attr('data-url');
             if(colSize==data.id)
                element.remove()

           });
           tbl_purchase_content= $("#tbody_purchaseRequest").html();
           $("#tbody_purchaseRequest").empty();
           var row=`<tr data-url=${data.id}><td></td><td>${tajhiz}</td><td>${part_name}</td><td>${part_qty}</td><td><i class="fa fa-close"></i></td><td> <div class="d-flex">
             <a href="#" class="btn btn-primary shadow btn-xs sharp mr-1 btn-sm js-update-purchaseRequestItem"   data-url="/PurchaseItem/${data.id}/update/"><i class="fa fa-pencil"></i></a>
              <a href="#" class="btn btn-danger shadow btn-xs sharp js-delete-purchase-item"  data-url="/PurchaseItem/${data.id}/delete/"><i class="fa fa-trash"></i></a>
        </div></td></tr>`;
        tbl_purchase_content+=row;
        // console.log(tbl_purchase_content);
        $("#tbody_purchaseRequest").html(tbl_purchase_content);

         }
         else if (data.delete) {


         }
         else {
           tbl_purchase_content= $("#tbody_purchaseRequest").html();
           $("#tbody_purchaseRequest").empty();
           var row=`<tr data-url=${data.id}><td></td><td>${tajhiz}</td><td>${part_name}</td><td>${part_qty}</td><td><i class="fa fa-close"></i></td><td> <div class="d-flex">
             <a href="#" class="btn btn-primary shadow btn-xs sharp mr-1 btn-sm js-update-purchaseRequestItem"   data-url="/PurchaseItem/${data.id}/update/"><i class="fa fa-pencil"></i></a>
              <a href="#" class="btn btn-danger shadow btn-xs sharp js-delete-purchase-item"  data-url="/PurchaseItem/${data.id}/delete/"><i class="fa fa-trash"></i></a>
        </div></td></tr>`;

           tbl_purchase_content+=row;
           // console.log(tbl_purchase_content);
           $("#tbody_purchaseRequest").html(tbl_purchase_content);
           ids.push(data.id);
           $("#lastPurchaseRequestid").val(ids);

         }
         //alert("Company created!");  // <-- This is just a placeholder for now for testing



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
 var saveSupplier=function(){
   $.ajax({
     url: form.attr("action"),
     data: form.serialize(),
     type: form.attr("method"),
     dataType: 'json',
     success: function (data) {
       console.log(data);
     }

   });
   return false;
 }

var deleteForm= function () {
    // alert("!23");
   var form = $(this);


   // var ijade_vaghfe=$("#checkkBoxId").attr("checked")?"<i class="fa fa-close"></i>":"";



   $.ajax({
     url: form.attr("action"),
     data: form.serialize(),
     type: form.attr("method"),
     dataType: 'json',
     error:function(x,y,z){
       // console.log(x.responseText);
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
       // console.log(form.parent());
       // form.parent().remove();
       tb=$("#purchaseRequest-table");
       tb.find("tr").each(function(index, element) {
         var colSize = $(element).attr('data-url');
         if(colSize==data.id)
            element.remove()

       });
      $("#modal-purchaseRequest").modal("hide");

         // $("#tbody_purchaseRequest").html(data.result);


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
$('#modal-purchaseRequest').on('click','.takepicture', function (event) {

  const video = $("#video");
  const snapBtn = $("#snap");
  const photo = $("#photo");
  
  let constraints = { audio: false, video: true };

  function takePicture() {
    const canvas = document.createElement("canvas");
    canvas.width = video[0].videoWidth;
    canvas.height = video[0].videoHeight;
    canvas.getContext("2d").drawImage(video[0], 0, 0);

    const imgData = canvas.toDataURL("image/png");
    photo.attr("src", imgData);
    photo.css("display", "block");
  }

  video.on("loadeddata", function() {
    snapBtn.on("click", async () => {
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      video[0].srcObject = stream;

      snapBtn.prop("disabled", true);
      takePicture();
    });

    
  });
});
$("#p-status").on("change",filter);
$(".js-create-purchaseRequest").click(myprLoader);
// $("#modal-purchaseRequest").on("click",'.js-create-supplier',loadsupplierform);
$("#modal-purchaseRequest").on("click",'.js-create-supplier',create_supplier);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-create-form", saveForm);
$("#mySupplierModal").on("submit",'.js-supplier-create',saveSupplier);

// Update book
$("#purchaseRequest-table").on("click", ".js-update-purchaseRequestItem", myprLoader);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-update-form", saveForm);
$("#modal-purchaseRequest").on("change", "#id_PurchaseRequestAssetMakan",loadRelatedAsset);
// Delete book
$("#purchaseRequest-table").on("click", ".js-delete-purchase-item", loadForm);
$("#modal-purchaseRequest").on("submit", ".js-purchaseRequest-delete-form", deleteForm);
$("#modal-purchaseRequest").on("change", "#id_PurchaseRequestAssetMakan",loadRelatedAsset);

$("#modal-purchaseRequest").on('click','.dz-button',function(){
  // alert("1");
 var myDropzone = new Dropzone("#dzdz", { url: 'file_upload_route'});

});
});
