$(document).ready(function () {

    var y;

    function create_token(){         
      var payload = {
        "username":"admin",
        "password":"admin"
    };

      $.ajax({
        url: "/api/token/",
        async: false,
        type: "POST",
        data: JSON.stringify(payload),
        cache: false,
        processData: false,
        contentType: "application/json",
        success: function (data) {
            // store tokens in localStorage
            //x=window.localStorage.setItem('refreshToken', data['refresh']);
            window.localStorage.setItem('accessToken', data['access']);
            y = data['access']
            //console.log(y);
        },
        error: function (rs, e) {
            console.error(rs.status);
            console.error(rs.responseText);
        }
    });
  };
    
  //create_token();
  //console.log("out",y);
        
    
    Date.prototype.today = function () { 
      return ((this.getDate() < 10)?"0":"") + this.getDate() +"/"+(((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) +"/"+ this.getFullYear();
  };
  
  // For the time now
  Date.prototype.timeNow = function () {
       return ((this.getHours() < 10)?"0":"") + this.getHours() +":"+ ((this.getMinutes() < 10)?"0":"") + this.getMinutes() +":"+ ((this.getSeconds() < 10)?"0":"") + this.getSeconds();
  };

  var datetime = new Date().today() + " @ " + new Date().timeNow();

  $('.time').text(datetime);

    function clear_form_elements(class_name) {
      jQuery("." + class_name)
        .find(":input")
        .each(function () {
          switch (this.type) {
            case "password":
            case "text":
            case "textarea":
            case "file":
            case "select-one":
            case "select-multiple":
            case "date":
            case "number":
            case "tel":
            case "email":
              jQuery(this).val("");
              break;
            case "checkbox":
            case "radio":
              this.checked = false;
              break;
          }
        });
    }

    // var today = new Date();
    // var dd = String(today.getDate()).padStart(2, '0');
    // var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    // var yyyy = today.getFullYear();
    // time = mm + '/' + dd + '/' + yyyy;

    $("body").on("click", ".lala", function () {
      var pk = this.id;
      $.ajax({
        url: "delete_data_nodes/" + pk + "/",
        data: {},
        type: "GET",
        contentType: "application/json",
        success: function (result) {
          $("#" + pk).remove();
        },
      });
    });

    $("#node2").hide();
    $("#node1").click(function () {
      $("#node2").click();
    });

    $("#add_node").click(function () {
      create_token();
      var payload_add = {
        machine: $("#machine").val(),
        location: $("#location").val(),
        sub_location: $("#sub_location").val(),
        uuid: $("#UID").val(),
        user_name: "{{ user.username }}",
        user_id: "{{ user.id }}",
        csrfmiddlewaretoken: "{{ csrf_token }}",
        tempreture_low: $("#tempreture_low").val(),
        tempreture_high: $("#tempreture_high").val(),

        humidity_low: $("#humidity_low").val(),
        humidity_high: $("#humidity_high").val(),
        CO2_high: $("#CO2_high").val(),
        CO2_low: $("#CO2_low").val(),
      };
      headers_payload = {'Authorization': 'Bearer ' + y,'Content-type':'application/json'};
      $.ajax({
        url: "/post_data_nodes",
        headers: headers_payload,
        type: "POST",
        data: JSON.stringify(payload_add),
        success: function (data, textStatus, jqXHR) {
          var x = `<div class="col-xl-4 col-lg-5 append_class" id="${data.id}">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div
                class="card-header py-3 d-flex flex-row align-items-center justify-content-between"
              >
                <h6 class="m-0 font-weight-bold text-primary">
                  UID : <a class="UID${data.id}"> ${data.uuid} </a>
                </h6>
                <h6 class="m-0 font-weight-bold text-primary"><a class="btn btn-success faulty" id="faulty${data.uuid}">Not Faulty</a></h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <h5 class="card-title">${data.user_name}</h5>
                <p class="card-text">
                  <b>machine : </b>
                  <a class="machine${data.id} text-secondary">
                    ${data.machine}
                  </a>
                </p>
                <p class="card-text">
                  <b>location : </b>
                  <a class="location${data.id} text-secondary">
                    ${data.location}
                  </a>
                </p>
                <p class="card-text">
                  <b>sub_location : </b>
                  <a class="sub_location${data.id} text-secondary">
                    ${data.sub_location}
                  </a>
                </p>
                <p class="card-text">
                  <b>humidity : </b>
                  <a class="humidity${data.id} text-secondary" id="humidity-${data.uuid}">
                    ${data.humidity}
                  </a>
                </p>
                <p class="card-text">
                  <b>tempreture : </b>
                  <a class="tempreture${data.id} text-secondary" id="tempreture-${data.uuid}">
                    ${data.tempreture}
                  </a>
                </p>
                <p class="card-text">
                  <b>battery : </b>
                  <a class="battery${data.id} text-secondary" id="battery-${data.uuid}">
                    ${data.battery}
                  </a>
                </p>
                <p class="card-text">
                  <b>C02 : </b>
                  <a class="CO2${data.id} text-secondary" id="CO2-${data.uuid}">
                    ${data.CO2}
                  </a>
                </p>
                {% for group in user.groups.all %} 
                {% if group.name == 'super admin' or group.name == 'admin' or group.name == 'user'%}
                <a class="btn btn-primary edit" id="${data.id}">Edit</a>
                <a class="btn btn-danger lala" id="${data.id}">Delete</a>
                <input type="hidden" id="tempreture_low${data.id}" value="${data.tempreture_low}"/>
                <input type="hidden" id="tempreture_high${data.id}" value="${data.tempreture_high}"/>
                <input type="hidden" id="humidity_high${data.id}" value="${data.humidity_high}"/>
                <input type="hidden" id="humidity_low${data.id}" value="${data.humidity_low}"/>
                <input type="hidden" id="CO2_low${data.id}" value="${data.CO2_low}"/>
                <input type="hidden" id="CO2_high${data.id}" value="${data.CO2_high}"/>
                {% endif %} 
                {% endfor %}
                <p class="card-text mt-2"><b>Last updated : </b>time</p>
                <div class="mt-4 text-center small">
                  <span class="mr-2">
                    <i class="fas fa-circle text-primary"></i> Direct
                  </span>
                  <span class="mr-2">
                    <i class="fas fa-circle text-success"></i> Social
                  </span>
                  <span class="mr-2">
                    <i class="fas fa-circle text-info"></i> Referral
                  </span>
                </div>
              </div>
            </div>
          </div>`;

          $("#appender").append(x);
          $("#close_node").click();
          clear_form_elements("modal-body");
        },
        error: function (jqXHR, textStatus, errorThrown) {
          alert(errorThrown);
        },
      });
    });

    $("body").on("click", ".edit", function () {
      pk = this.id;

      var payload = {
        machine: $(".machine" + pk).text(),
        location: $(".location" + pk).text(),
        sub_location: $(".sub_location" + pk).text(),
        uid: $(".UID" + pk).text(),
        tempreture_low: $("#tempreture_low"+pk).val(),
        tempreture_high: $("#tempreture_high"+pk).val(),
        humidity_low: $("#humidity_low"+pk).val(),
        humidity_high: $("#humidity_high"+pk).val(),
        CO2_high: $("#CO2_high"+pk).val(),
        CO2_low: $("#CO2_low"+pk).val(),
        csrfmiddlewaretoken: "{{ csrf_token }}",
      };
     //console.log(payload)
      var y = `<div class="col-xl-4 col-lg-5 append_class" id="${pk}">
        <div class="card shadow mb-4">
            <!-- Card Header - Dropdown -->
            <div
                class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <div class="form-group row">
                    <label for="UID" class="col-sm-5 col-form-label">UID</label>
                    <div class="col-sm-7">
                      <input type="text" class="form-control UID${pk}" id="UID" value="${payload.uid}">
                    </div>
                  </div>
            </div>
            <!-- Card Body -->
            <div class="card-body">
                <form>
                    
                    <div class="form-group row">
                      <label for="machine" class="col-sm-3 col-form-label">machine</label>
                      <div class="col-sm-9">
                        <input type="text" class="form-control machine${pk}" id="machine" value="${payload.machine}">
                      </div>
                    </div>
                    <div class="form-group row">
                      <label for="location" class="col-sm-3 col-form-label">location</label>
                      <div class="col-sm-9">
                        <input type="text" class="form-control location${pk}" id="location" value="${payload.location}">
                      </div>
                    </div>
                    <div class="form-group row">
                        <label for="sub_location" class="col-sm-3 col-form-label">sub_location</label>
                        <div class="col-sm-9">
                          <input type="text" class="form-control sub_location${pk}" id="sub_location" value="${payload.sub_location}">
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="sub_location" class="col-sm-3 col-form-label">tempreture</label>
                        <div class="col-sm-9">
                          <div class="row">
                            <div class="col">
                              <input type="text" class="form-control tempreture_low${pk}" placeholder="low" id="" value="${payload.tempreture_low}">
                            </div>
                            <div class="col">
                              <input type="text" class="form-control tempreture_high${pk}" placeholder="high" id="" value="${payload.tempreture_high}">
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="sub_location" class="col-sm-3 col-form-label">humidity</label>
                        <div class="col-sm-9">
                          <div class="row">
                            <div class="col">
                              <input type="text" class="form-control humidity_low${pk}" placeholder="low" id="" value="${payload.humidity_low}">
                            </div>
                            <div class="col">
                              <input type="text" class="form-control humidity_high${pk}" placeholder="high" id="" value="${payload.humidity_high}">
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="sub_location" class="col-sm-3 col-form-label">CO2</label>
                        <div class="col-sm-9">
                          <div class="row">
                            <div class="col">
                              <input type="text" class="form-control CO2_low${pk}" placeholder="low" id="" value="${payload.CO2_low}">
                            </div>
                            <div class="col">
                              <input type="text" class="form-control CO2_high${pk}" placeholder="high" id="" value="${payload.CO2_high}">
                            </div>
                          </div>
                        </div>
                      </div>
                    <div class="form-group row">
                      <div class="col-sm-3">
                        <a class="btn btn-primary my-2 save-btn" id="${pk}">submit</a>
                      </div>
                      <div class="col-sm-3">
                        <a class="btn btn-danger my-2 close-btn" id="${pk}">close</a>
                      </div>
                    </div>
                  </form>
                <p class="card-text mt-2"><b>Last updated : </b>time</p>
                <div class="mt-4 text-center small">
                    <span class="mr-2">
                        <i class="fas fa-circle text-primary"></i> Direct
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle text-success"></i> Social
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle text-info"></i> Referral
                    </span>
                </div>
            </div>
        </div>
    </div>`;

      $("append_class,#" + pk).replaceWith(y);
    });

    $("body").on("click", ".close-btn", function (e) {
      e.preventDefault();
      pk = this.id;

      var payload = {
        machine: $(".machine" + pk).text(),
        location: $(".location" + pk).text(),
        sub_location: $(".sub_location" + pk).text(),
        uid: $(".UID" + pk).text(),
        tempreture_low: $("#tempreture_low"+pk).val(),
        tempreture_high: $("#tempreture_high"+pk).val(),
        humidity_low: $("#humidity_low"+pk).val(),
        humidity_high: $("#humidity_high"+pk).val(),
        CO2_high: $("#CO2_high"+pk).val(),
        CO2_low: $("#CO2_low"+pk).val(),
        csrfmiddlewaretoken: "{{ csrf_token }}",
      };

      $.ajax({
        url: "/get_single_node/" + pk,
        data: {},
        type: "GET",
        contentType: "application/json",
        success: function (result) {
          //console.log(result[0].id)
          //alert("Data: " + data + "\nStatus: " + status);
          var data = result[0];
          var z = `<div class="col-xl-4 col-lg-5 append_class" id="${data.id}">
            <div class="card shadow mb-4">
              <!-- Card Header - Dropdown -->
              <div
                class="card-header py-3 d-flex flex-row align-items-center justify-content-between"
              >
                <h6 class="m-0 font-weight-bold text-primary">
                  UID : <a class="UID${data.id}"> ${data.uuid} </a>
                </h6>
                <h6 class="m-0 font-weight-bold text-primary"><a class="btn btn-success faulty" id="faulty${data.uuid}">Not Faulty</a></h6>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <h5 class="card-title">${data.user_name}</h5>
                <p class="card-text">
                  <b>machine : </b>
                  <a class="machine${data.id} text-secondary">
                    ${data.machine}
                  </a>
                </p>
                <p class="card-text">
                  <b>location : </b>
                  <a class="location${data.id} text-secondary">
                    ${data.location}
                  </a>
                </p>
                <p class="card-text">
                  <b>sub_location : </b>
                  <a class="sub_location${data.id} text-secondary">
                    ${data.sub_location}
                  </a>
                </p>
                <p class="card-text">
                  <b>humidity : </b>
                  <a class="humidity${data.id} text-secondary" id="humidity-${data.uuid}">
                    ${data.humidity}
                  </a>
                </p>
                <p class="card-text">
                  <b>tempreture : </b>
                  <a class="tempreture${data.id} text-secondary" id="tempreture-${data.uuid}">
                    ${data.tempreture}
                  </a>
                </p>
                <p class="card-text">
                  <b>battery : </b>
                  <a class="battery${data.id} text-secondary" id="battery-${data.uuid}">
                    ${data.battery}
                  </a>
                </p>
                <p class="card-text">
                  <b>C02 : </b>
                  <a class="CO2${data.id} text-secondary" id="CO2-${data.uuid}">
                    ${data.CO2}
                  </a>
                </p>
                {% for group in user.groups.all %} 
                {% if group.name == 'super admin' or group.name == 'admin' or group.name == 'user'%}
                <a class="btn btn-primary edit" id="${data.id}">Edit</a>
                <a class="btn btn-danger lala" id="${data.id}">Delete</a>
                <input type="hidden" id="tempreture_low${data.id}" value="${data.tempreture_low}"/>
                <input type="hidden" id="tempreture_high${data.id}" value="${data.tempreture_high}"/>
                <input type="hidden" id="humidity_high${data.id}" value="${data.humidity_high}"/>
                <input type="hidden" id="humidity_low${data.id}" value="${data.humidity_low}"/>
                <input type="hidden" id="CO2_low${data.id}" value="${data.CO2_low}"/>
                <input type="hidden" id="CO2_high${data.id}" value="${data.CO2_high}"/>
                {% endif %} 
                {% endfor %}
                <p class="card-text mt-2"><b>Last updated : </b>time</p>
                <div class="mt-4 text-center small">
                  <span class="mr-2">
                    <i class="fas fa-circle text-primary"></i> Direct
                  </span>
                  <span class="mr-2">
                    <i class="fas fa-circle text-success"></i> Social
                  </span>
                  <span class="mr-2">
                    <i class="fas fa-circle text-info"></i> Referral
                  </span>
                </div>
              </div>
            </div>
          </div>`;

          $("append_class,#" + pk).replaceWith(z);
        },
      });
    });


    {% comment %} $("body").on("click", ".save-btn", function () {
        pk=this.id
        var payload = {
          machine: $(".machine" + pk).val(),
          location: $(".location" + pk).val(),
          sub_location: $(".sub_location" + pk).val(),
          uuid: $(".UID" + pk).val(),
          tempreture_low: $(".tempreture_low"+pk).val(),
          tempreture_high: $(".tempreture_high"+pk).val(),
          humidity_low: $(".humidity_low"+pk).val(),
          humidity_high: $(".humidity_high"+pk).val(),
          CO2_high: $(".CO2_high"+pk).val(),
          CO2_low: $(".CO2_low"+pk).val(),
          csrfmiddlewaretoken: "{{ csrf_token }}",
          };
          console.log(payload)
        $.ajax({
          url: "/update_single_node/"+pk+"/",
          type: "PUT",
          //data: JSON.stringify({payload:payload}),
          data : payload,
          success: function (data, textStatus, jqXHR) {
            var x1 = `<div class="col-xl-4 col-lg-5 append_class" id="${data.id}">
              <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                  class="card-header py-3 d-flex flex-row align-items-center justify-content-between"
                >
                  <h6 class="m-0 font-weight-bold text-primary">
                    UID : <a class="UID${data.id}"> ${data.uuid} </a>
                  </h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                  <h5 class="card-title">${data.user_name}</h5>
                  <p class="card-text">
                    <b>machine : </b>
                    <a class="machine${data.id} text-secondary">
                      ${data.machine}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>location : </b>
                    <a class="location${data.id} text-secondary">
                      ${data.location}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>sub_location : </b>
                    <a class="sub_location${data.id} text-secondary">
                      ${data.sub_location}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>humidity : </b>
                    <a class="humidity${data.id} text-secondary">
                      ${data.humidity}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>tempreture : </b>
                    <a class="tempreture${data.id} text-secondary">
                      ${data.tempreture}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>battery : </b>
                    <a class="battery${data.id} text-secondary">
                      ${data.battery}
                    </a>
                  </p>
                  <p class="card-text">
                    <b>C02 : </b>
                    <a class="CO2${data.id} text-secondary">
                      ${data.CO2}
                    </a>
                  </p>
                  {% for group in user.groups.all %} 
                  {% if group.name == 'super admin' or group.name == 'admin' or group.name == 'user'%}
                  <a class="btn btn-primary edit" id="${data.id}">Edit</a>
                  <a class="btn btn-danger lala" id="${data.id}">Delete</a>
                  <input type="hidden" id="tempreture_low${data.id}" value="${data.tempreture_low}"/>
                  <input type="hidden" id="tempreture_high${data.id}" value="${data.tempreture_high}"/>
                  <input type="hidden" id="humidity_high${data.id}" value="${data.humidity_high}"/>
                  <input type="hidden" id="humidity_low${data.id}" value="${data.humidity_low}"/>
                  <input type="hidden" id="CO2_low${data.id}" value="${data.CO2_low}"/>
                  <input type="hidden" id="CO2_high${data.id}" value="${data.CO2_high}"/>
                  {% endif %} 
                  {% endfor %}
                  <p class="card-text mt-2"><b>Last updated : </b>time</p>
                  <div class="mt-4 text-center small">
                    <span class="mr-2">
                      <i class="fas fa-circle text-primary"></i> Direct
                    </span>
                    <span class="mr-2">
                      <i class="fas fa-circle text-success"></i> Social
                    </span>
                    <span class="mr-2">
                      <i class="fas fa-circle text-info"></i> Referral
                    </span>
                  </div>
                </div>
              </div>
            </div>`;

                  $("append_class,#" + pk).replaceWith(x1);
          },
          error: function (jqXHR, textStatus, errorThrown) {
            alert(errorThrown);
          },
        });

    }); {% endcomment %}


    function get_data(uid,user_name){
      //console.log("1"),
      $.ajax({
        url: "/send_node_data/"+uid+'/'+user_name,
        data: {},
        type: "GET",
        contentType: "application/json",
        success: function (result){
          //console.log(result[0]['fields'])
          var u = result[0]['fields']['uuid'];
          var b = result[0]['fields']['battery'];
          var t = result[0]['fields']['tempreture'];
          var h = result[0]['fields']['humidity'];
          var c = result[0]['fields']['CO2'];

          var th = result[0]['fields']['tempreture_high'];
          var hh = result[0]['fields']['humidity_high'];
          var ch = result[0]['fields']['CO2_high'];

          var tl = result[0]['fields']['tempreture_low'];
          var hl = result[0]['fields']['humidity_low'];
          var cl = result[0]['fields']['CO2_low'];

          $('#tempreture-'+u).text(t);
          $('#humidity-'+u).text(h);
          $('#battery-'+u).text(b);
          $('#CO2-'+u).text(c);

          if (Number(t) > Number(th) || Number(t) < Number(tl) || Number(h) > Number(hh) || Number(h) < Number(hl) || Number(c) > Number(ch) || Number(c) < Number(cl)) {
            $('#faulty'+u).text('Faulty')
            $('#faulty'+u).removeClass('btn-success')
            $('#faulty'+u).removeClass('btn-danger')
            $('#faulty'+u).addClass('btn-danger')
          }
          else{

            $('#faulty'+u).text('Not Faulty')
            $('#faulty'+u).removeClass('btn-danger')
            $('#faulty'+u).removeClass('btn-success')
            $('#faulty'+u).addClass('btn-success')
          };

          $('#time'+u).text(datetime);
                        
        }
      });};


      function run_data(){

        $.ajax({
          url: "/all_data/",
          data: {},
          type: "GET",
          contentType: "application/json",
          success: function (result){
            //console.log(result)  
            
            for (let i = 0; i < result.length; i++) {

              //console.log(result[i]['fields']['uuid']);

              var uid = result[i]['fields']['uuid'];
              var user_name = result[i]['fields']['user_name'];
              get_data(uid,user_name);
            }
            
          }
        });};



      setInterval( run_data, 1000);

      //---------------------------------------------------------------------------------------------------------------------





      Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
// *     example: number_format(1234.56, 2, ',', ' ');
// *     return: '1 234,56'
number = (number + '').replace(',', '').replace(' ', '');
var n = !isFinite(+number) ? 0 : +number,
prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
s = '',
toFixedFix = function(n, prec) {
  var k = Math.pow(10, prec);
  return '' + Math.round(n * k) / k;
};
// Fix for IE parseFloat(0.55).toFixed(0) = 0;
s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
if (s[0].length > 3) {
s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
}
if ((s[1] || '').length < prec) {
s[1] = s[1] || '';
s[1] += new Array(prec - s[1].length + 1).join('0');
}
return s.join(dec);
}

// Area Chart Example
function graph (label,data1){
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
type: 'line',
data: {
labels: label,
datasets: [{
  label: "Earnings",
  lineTension: 0.3,
  backgroundColor: "rgba(78, 115, 223, 0.05)",
  borderColor: "rgba(78, 115, 223, 1)",
  pointRadius: 3,
  pointBackgroundColor: "rgba(78, 115, 223, 1)",
  pointBorderColor: "rgba(78, 115, 223, 1)",
  pointHoverRadius: 3,
  pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
  pointHoverBorderColor: "rgba(78, 115, 223, 1)",
  pointHitRadius: 10,
  pointBorderWidth: 2,
  data: data1,
}],
},
options: {
maintainAspectRatio: false,
layout: {
  padding: {
    left: 10,
    right: 25,
    top: 25,
    bottom: 0
  }
},
scales: {
  xAxes: [{
    time: {
      unit: 'date'
    },
    gridLines: {
      display: false,
      drawBorder: false
    },
    ticks: {
      maxTicksLimit: 7
    }
  }],
  yAxes: [{
    ticks: {
      maxTicksLimit: 5,
      padding: 10,
      // Include a dollar sign in the ticks
      callback: function(value, index, values) {
        return number_format(value);
      }
    },
    gridLines: {
      color: "rgb(234, 236, 244)",
      zeroLineColor: "rgb(234, 236, 244)",
      drawBorder: false,
      borderDash: [2],
      zeroLineBorderDash: [2]
    }
  }],
},
legend: {
  display: false
},
tooltips: {
  backgroundColor: "rgb(255,255,255)",
  bodyFontColor: "#858796",
  titleMarginBottom: 10,
  titleFontColor: '#6e707e',
  titleFontSize: 14,
  borderColor: '#dddfeb',
  borderWidth: 1,
  xPadding: 15,
  yPadding: 15,
  displayColors: false,
  intersect: false,
  mode: 'index',
  caretPadding: 10,
  callbacks: {
    label: function(tooltipItem, chart) {
      var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
      return  number_format(tooltipItem.yLabel);
    }
  }
}
}
});};


  var y;

    function create_token(){         
      var payload = {
        "username":"admin",
        "password":"admin"
    };

      $.ajax({
        url: "/api/token/",
        async: false,
        type: "POST",
        data: JSON.stringify(payload),
        cache: false,
        processData: false,
        contentType: "application/json",
        success: function (data) {
            // store tokens in localStorage
            //x=window.localStorage.setItem('refreshToken', data['refresh']);
            window.localStorage.setItem('accessToken', data['access']);
            y = data['access']
            //console.log(y);
        },
        error: function (rs, e) {
            console.error(rs.status);
            console.error(rs.responseText);
        }
    });
  };



$("#senddata").click(function (e) {
e.preventDefault();
create_token();
var payload_add = {
uuid: $("#uuid_graph").val(),
field: $("#field").val(),
start_date: $("#start_date").val(),
end_date: $("#end_date").val(),    
};
headers_payload = {'Authorization': 'Bearer ' + y,'Content-type':'application/json'};
$.ajax({
url: "/graph"+"/",
headers: headers_payload,
type: "POST",
data: JSON.stringify(payload_add),
success: function (data, textStatus, jqXHR) {
  
  var label1 = [];
  var data2 = [];
  

  for (let i = 0; i < data.length; i++) {
    label1.push(data[i]["fields"]["date"]);
    data2.push(data[i]["fields"][payload_add.field]);

    var uuid = data[i]['fields']['uuid'];
    var battery = data[i]['fields']['battery'];
    var tempreture = data[i]['fields']['tempreture'];
    var humidity = data[i]['fields']['humidity'];
    var CO2 = data[i]['fields']['CO2'];
    var date = data[i]['fields']['date'];
    var time = data[i]['fields']['time'];
    var battery = data[i]['fields']['battery'];

    $("#table-report").append(`<tr>
      <th scope="row">${i}</th>
      <td>${date}</td>
      <td>${time}</td>
      <td>${uuid}</td>
      <td>${tempreture}</td>
      <td>${CO2}</td>
      <td>${battery}</td>
    </tr>`);

  };
  $("#myAreaChart").remove()
  $("#graph_div").append(`<canvas id="myAreaChart"></canvas>`)
  graph (label1,data2);

},
error: function (jqXHR, textStatus, errorThrown) {
  alert(errorThrown);
},

});});


$("#print_graph").click(function (e){
e.preventDefault();
var HTML_Width = $("#pdf").width();
    var HTML_Height = $("#pdf").height();
    var top_left_margin = 15;
    var PDF_Width = HTML_Width+(top_left_margin*2);
    var PDF_Height = (PDF_Width*1.5)+(top_left_margin*2);
    var canvas_image_width = HTML_Width;
    var canvas_image_height = HTML_Height;
    
    var totalPDFPages = Math.ceil(HTML_Height/PDF_Height)-1;
    

    html2canvas($(".canvas_div_pdf")[0],{allowTaint:true}).then(function(canvas) {
        canvas.getContext('2d');
        
        console.log(canvas.height+"  "+canvas.width);
        
        
        var imgData = canvas.toDataURL("image/jpeg", 1.0);
        var pdf = new jsPDF('p', 'pt',  [PDF_Width, PDF_Height]);
        pdf.addImage(imgData, 'JPG', top_left_margin, top_left_margin,canvas_image_width,canvas_image_height);
        
        
        for (var i = 1; i <= totalPDFPages; i++) { 
            pdf.addPage(PDF_Width, PDF_Height);
            pdf.addImage(imgData, 'JPG', top_left_margin, -(PDF_Height*i)+(top_left_margin*4),canvas_image_width,canvas_image_height);
        }
        
        pdf.save("HTML-Document.pdf");
    });

});


$("#print_table").click(function (e){
e.preventDefault();
var HTML_Width = $("#table_pdf").width();
var HTML_Height = $("#table_pdf").height();
var top_left_margin = 15;
var PDF_Width = HTML_Width+(top_left_margin*2);
var PDF_Height = (PDF_Width*1.5)+(top_left_margin*2);
var canvas_image_width = HTML_Width;
var canvas_image_height = HTML_Height;

var totalPDFPages = Math.ceil(HTML_Height/PDF_Height)-1;


html2canvas($("#table_pdf")[0],{allowTaint:true}).then(function(canvas) {
canvas.getContext('2d');

console.log(canvas.height+"  "+canvas.width);


var imgData = canvas.toDataURL("image/jpeg", 1.0);
var pdf = new jsPDF('p', 'pt',  [PDF_Width, PDF_Height]);
  pdf.addImage(imgData, 'JPG', top_left_margin, top_left_margin,canvas_image_width,canvas_image_height);


for (var i = 1; i <= totalPDFPages; i++) { 
  pdf.addPage(PDF_Width, PDF_Height);
  pdf.addImage(imgData, 'JPG', top_left_margin, -(PDF_Height*i)+(top_left_margin*4),canvas_image_width,canvas_image_height);
}

  pdf.save("Document.pdf");
  });

});


      
      $("body").on("click", "#1", function (){
        $(".1").removeClass("d-none")
        $(".2").addClass("d-none")
       });

       $("body").on("click", "#2", function (){
        $(".2").removeClass("d-none")
        $(".1").addClass("d-none")
       });
  
  
    })