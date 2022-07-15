$(function(){

  // $('.dtpicker').bootstrapMaterialDatePicker({
  //       weekStart: 0,
  //       time: false,
  //       nowButton : true,
  //       initialValue: true,
  //       initialValueType: 'gregorian',
  //   });
    $("#id_PurchaseDateTo").pDatepicker({

            format: 'YYYY-MM-DD',
            initialValueType: 'gregorian',
            autoClose:true

    });

    var save_msg=function(){
     document.getElementById('purchaseform').submit();
    }
    var update=function(){
      window.location=$(this).attr('data-url');
    }
    $(".sub_purchase").on("click",  save_msg);
    $("#purchaseRequest-table").on("click", ".js-update-purchaseRequest", update);
});
