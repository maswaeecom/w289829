$(document).ready(function() {
    timer();

    $("#totalchips").keyup(function() { 
      var betamount1 = $(this).val(); 
      var getbalance = $('#getbalance').val();
      //alert(betamount1);
      if(parseInt(betamount1) > parseInt(getbalance)){
        alert("Amount is Bigger Then Balance");
      }
      else {
      var finalbalance = getbalance - betamount1;
      var setbalance = document.getElementById("availablebalance"); // get
      setbalance.innerHTML="<p> Available Chips: " + finalbalance + "</p>";
       
      }  
    });
  
  
  
    $(".even").click(function() {   
      $(".alleven").css('background-color', '#429051');
      $(".allodd").css('background-color', '#651718');
      
    });
  
    $(".odd").click(function() {   
      $(".allodd").css('background-color', '#d31515');
      $(".alleven").css('background-color', '#244e2c');
    });
  
    $('#help').click(function(){
      $('#helpmodal').modal('show');
    });

    
     $(".btncontent").click(function() {
     $('#mymodal').modal('show');
      var btnvalue = $(this).text().trim();
      if(btnvalue=="Even" || btnvalue=="Odd"){
      $('#totalbetamount').val(500);
      $('#selectedbetnumber').val(btnvalue);
      $('#totalchips').val(500);

      var getbalance = $('#getbalance').val();
    var setbalance = document.getElementById("availablebalance"); // get
    setbalance.innerHTML="<p> Available Chips: " + getbalance + "</p>";
      var selectednumber = document.getElementById("selectednumber"); // get
      selectednumber.innerHTML="<p> Selected Item: " + btnvalue + "</p>"; 
      var totalchipstext = document.getElementById("totalchips"); // get
      totalchipstext.innerHTML="<p> Total Chips: " + 50 + "</p>"; 
     
  
     $(".betamount").click(function() {
      var betamount = $(this).text();
      $('#totalbetamount').val(betamount * 50);
      $('#totalchips').val(betamount * 50);
      //var totalchipstext = document.getElementById("totalchips"); // get
      // totalchipstext.innerHTML="<p> Total Chips: " + betamount * 5 + "</p>";
      totalchipstext.val=betamount * 5 ;
      console.log(betamount);
      var getbalance = $('#getbalance').val();
      var finalbalance = getbalance -betamount;
     
      var setbalance = document.getElementById("availablebalance"); // get
      setbalance.innerHTML="<p> Available Chips: " + finalbalance + "</p>"; 
       
     });    
      
    }
    else {
      $('#totalbetamount').val(10);
      $('#selectedbetnumber').val(btnvalue);
      $('#totalchips').val(10);
      var selectednumber = document.getElementById("selectednumber"); // get
      selectednumber.innerHTML="<p> Selected Item: " + btnvalue + "</p>"; 
      // var totalchipstext = document.getElementById("totalchips"); // get
      // totalchipstext.innerHTML="<p> Total Chips: " + 10 + "</p>"; 
  
      $(".betamount").click(function() {
        var betamount = $(this).text().trim();
        $('#totalbetamount').val(betamount);
        $('#totalchips').val(betamount);
        // var totalchipstext = document.getElementById("totalchips"); // get
        // totalchipstext.innerHTML="<p> Total Chips: " + betamount + "</p>"; 
  
        console.log(betamount);
         
       });
      
    }
      
     });
  
     
  
     $('#placebetbtn').click(function(){
      var userid = $('#userid').val();
      var period = $('#periodid').text();
      var timing = $('#timing').val();
      var number = $('#selectedbetnumber').val();
      var amount = $('#totalchips').val();
  
      var mi = $('#mint').val();
      var sec = $('#seconds').val();

      // alert(number);

      // if(number=="Even" || number=="Odd"){
      //   if((amount % 50) != 0){
     
      //     console.log("multiple have");
      //     $('#10multiple99').modal('show');
      //   }
      // }


      if((amount % 50) != 0 && number=="Even"){
     
        console.log("multiple");
        $('#10multiple99').modal('show');
      }

      else if((amount % 50) != 0 && number=="Odd"){
     
        console.log("multiple");
        $('#10multiple99').modal('show');
      }

      else {
      if(mi < 1 && sec < 30 ){
       
        $('#mymodal').modal('hide');
        $('#timemodal').modal('show');
      }
      else { 

      $.ajax({
          url: "placebet99",
          type: "POST",
          dataType: "json",
          data: JSON.stringify({uid:userid, amt:amount, period:period, type:number, timing:timing}),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
          },
          success: (data) => {
             
              if(data.status=="success"){
              console.log(data);
              $('#mymodal').modal('hide');
              $('#betplaced').modal('show');
              setTimeout(function(){
                $('#betplaced').modal('hide')
              }, 3000);
              
              }
              else if (data.status=="0") {
                console.log('low balance');
                
                $('#mymodal').modal('hide');
                $('#balancemodal').modal('show');
              }
            else{
              console.log("check");
              $('#mymodal').modal('hide');
            }
  
          },
          error: (error) => {
            console.log(error);
          }
        });
      }
    }
      
     });
  
  
  
  });
  
  
  // $(document).ready(function() {
  
  //     $(".form-check-radio").click(function(){
  //         var val = $("input[type='radio']:checked").val();
  //         alert(val);
  //     });
  // });
  
  
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + "=")) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
    function pad(n) {
      return (n < 10 ? '0' : '') + n;
    }
  
    function calcTime(offset){
      var b = new Date()
      var utc = b.getTime()+(b.getTimezoneOffset()*60000);
      var nd = new Date(utc+(3600000*offset));
      return nd.toLocaleString();
  
    }
  
  
  
  async function timer(){
  
    $.ajax({
      url: "getlottery99",
      type: "GET",
      dataType: "json",
      success: (data) => {
      console.log(data);
      console.log(data.lastresult);
          if(data.id > 0 ){
       
            var createddate = new Date(data.created_at).getTime();
            var expireddate = new Date(data.expired_at).getTime();
            var periodidtext = document.getElementById("periodid"); // get
            periodidtext.innerHTML= data.id;

            if(data.lastresult % 2 == 0){
              $("#resb").addClass("childeven");
              $("#resb").addClass("child15");
              $('#result99').text(data.lastresult);
            }
            else {
              $("#resb").addClass("childodd");
              $("#resb").addClass("child15");
              $('#result99').text(data.lastresult);

            }
            
            // $("#resultball").removeClass("child15");
            // $("#resultballsmall").removeClass("child15");
            // // $("#resultball").attr("src","../../static/game/img/balls/"+ evenoddimg +".png").addClass("child15, childeven");
            // $("#resb").addClass("childeven");
            // $("#resb").addClass("child15");
            // $('#result99').text(data.lastresult);
            // $("#resultballsmall").attr("src","../../static/game/img/balls/"+ evenoddimg +".png").addClass("child15");
  
          
            //$(".resultballsmall").effect( "bounce",{times:3}, 300 );
         
    
            var mytable = document.getElementById("mytable"); // get
            
            var i = 0;
            var table = '<table class="table table-dark" style="color:gold"> <thead><tr><th style="color:gold"> Period </th><th style="color:gold"> Price </th><th style="color:gold"> Color </th><th style="color:gold"> Number </th></tr></thead>';
              $.each(JSON.parse(data.resdata), function (index, value) {
                console.log(data.resdata);
              // var mytable = document.getElementById("mytable");
              // mytable.innerHTML = "<td>" + value.fields.period + "</td><td>" + 38773 + "</td><td>" + value.fields.result + "</td><td>" + value.fields.result + "</td>";
              // console.log(value.fields.period);
              var cir = "";
              if(value.fields.result % 2 == 0){
                cir = "<span class='doteven'></span>";
              }
              else {
                cir = "<span class='dotodd'></span>";
              }
              var rnum = Math.floor(10000 + Math.random() * 90000);
              table += ('<tr>');
              table += ('<td>' + value.fields.period + '</td>');
              table += ('<td>' + value.fields.price + '</td>');
              table += ('<td>' + cir + '</td>');
              table += ('<td>' + value.fields.result + '</td>');
              table += ('</tr>');
                
                });

                table += ('<tr>');
                table += ('<td colspan=5 style="text-align:right"><a href="result99"><button class="btn btn-xs btn-success">More</button</a></td>');
                table += ('</tr>');
  
                table += '</table>'; 
  
                $('#mytable').html(table);
  
            
            var x = setInterval(function() {
            
              // Get today's date and time
              var now = new Date().getTime();
              // maintime = calcTime('+11');
              // var now = new Date(maintime).getTime()
              // console.log(new Date(maintime).getTime());
  
              // Find the distance between now and the count down date
              var distance =  expireddate - now;
              //console.log(distance);
              
  
  
  
  
  
              // Time calculations for days, hours, minutes and seconds
              var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
              var seconds = Math.floor((distance % (1000 * 60)) / 1000);
              //console.log(minutes)  
              var countdown = document.getElementById("tiles"); // get
              countdown.innerHTML = "<span>" + minutes + "</span>:<span>" + seconds + "</span>"; 
            
              $('#mint').val(minutes);
              $('#seconds').val(seconds);

              if (distance <  0) {
        
                $.ajax({
                    url: "getlottery99",
                    type: "GET",
                    dataType: "json",
                    success: (data) => {
                        if(data.id > 0 ){
                          $('#expiredat').val(data.date);
                        //console.log(data);
                        timer()
                      }
                    },
                    error: (error) => {
                      console.log(error);
                    }
                  });
        
                
                clearInterval(x);
                countdown.innerHTML = "<span>" + 0 + "</span><span>" + 0 + "</span>";
                // document.getElementById("demo").innerHTML = "EXPIRED";
              }
            }, 1000);
          
        }
      },
      error: (error) => {
        console.log(error);
      }
    }); 
    
    
  
  }
  
  
  
  