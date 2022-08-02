let stop_timer1 = true;
let ex_counter = 0;
let ex_status = 0;
let gas_in_flag = false;
let recovery_flag = false;
let ex_555_func_run = false;
let ex_585_func_run = false;
let timeout_list = [];

function stop_btn_func() 
{
  stop_timer1 = false;
  ex_status=0;
  ex_counter = 0;
  ex_555_func_run = false;
  ex_585_func_run = false;
}
function allday_btn_func() 
{
  stop_timer1 = true
  if (stop_timer1 == true)
  {
    allday_btn_timer_promise();
  }
}

function allday_btn_timer_promise() 
{
  function allday_btn_ajax() 
  {

    return  new Promise(function(resolve, reject) 
    {
      var data =
      {
        'btn' : 'allday',
      }
      $.ajax
      ({
        type: "POST",
        url: "/",
        data: JSON.stringify(data, null, '\t'),
        contentType: 'application/json;charset=UTF-8',
        success: function(result) 
        {
          console.log('ajax successed');
        },
        error: function(result) 
        {
          console.log('ajax error');
        }
      })
      .done(resolve)
      .fail(reject);
    });
  }

  function timer_60s() 
  {
    return new Promise(function (resolve, reject) 
    {
      console.log("In the timer function");
      let count = 60;
      timer1 = setInterval(function () 
      {
        count--;
        console.log(count, "timer running");
        if (count == 0) 
        {
          resolve('Time is up');
          clearInterval(timer1);
          count = 60;
        }
      }, 1000);
    });
  }
  var p1 = allday_btn_ajax();
  var p2 = timer_60s();
  Promise.all([p1, p2]).then(values => 
  {
    console.log("values : ",values); 
    if (stop_timer1 == true)
    {
      retry_allday_btn_timer_promise();
    }
    else
    {
      console.log('stop')
    }
  });
}
function retry_allday_btn_timer_promise()
{
  allday_btn_timer_promise();  
}


function timeout_list_selector()
{
  if (ex_555_func_run)
  {
    timeout_list = [300, 300, 300];
  }
  else if (ex_585_func_run)
  {
    timeout_list = [300, 480, 300];
  }
  
}

function ex555_func() 
{
  stop_timer1 = true;
  ex_555_func_run = true;
  timeout_list_selector();
  if (stop_timer1 == true)
  {
    ex_btn_timer1s_promise();
  }
}

function ex585_func() 
{
  stop_timer1 = true;
  ex_585_func_run = true;
  timeout_list_selector();
  if (stop_timer1 == true)
  {
    ex_btn_timer1s_promise();
  }
}



function gas_in_ajax_promise() 
{
  function gas_in_ajax() //AJAX_switch_sample
  {
    return new Promise(function (resolve, reject) 
    {
      var data =
      {
        'btn': 'switch_sample',
      }
      $.ajax
        ({
          type: "POST",
          url: "/",
          data: JSON.stringify(data, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          success: function (result) 
          {
            console.log('ajax successed_switch_sample');
          },
          error: function (result) 
          {
            console.log('ajax error');
          }
        })
        .done(resolve)
        .fail(reject);
    });
  }

  var p5 = gas_in_ajax();
  Promise.all([p5]).then(values => 
  {
    console.log(values);
    ex_counter = 0;
    gas_in_flag = false;
    ex_status = 1;
    //console.log('ex_status = ', ex_status);
    if (stop_timer1 == true)
    {
      retry_ex_btn_timer1s_promise();
    }
  });
}

function recovery_ajax_promise() 
{
  function recovery_ajax() //AJAX_switch_purge
  {
    return new Promise(function (resolve, reject) 
    {
      var data =
      {
        'btn': 'switch_purge',
      }
      $.ajax
        ({
          type: "POST",
          url: "/",
          data: JSON.stringify(data, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          success: function (result) 
          {
            console.log('ajax successed_switch_purge');
          },
          error: function (result) 
          {
            console.log('ajax error');
          }
        })
        .done(resolve)
        .fail(reject);
    });
  }

  var p6 = recovery_ajax();
  Promise.all([p6]).then(values => 
  {
    console.log(values);
    ex_counter = 0;
    recovery_flag = false;
    ex_status = 2;
    //console.log('ex_status = ', ex_status);
    if (stop_timer1 == true)
    {
      retry_ex_btn_timer1s_promise();
    }
  });
}



function ex_btn_timer1s_promise() 
{
  function ex_btn_ajax() 
  {
    return new Promise(function (resolve, reject) 
    {
      var text1 = document.querySelector("[name='input_text']").value;
      var data =
      {
        'btn': 'ex',
        'input_gas' : text1,
      }
      $.ajax
        ({
          type: "POST",
          url: "/",
          data: JSON.stringify(data, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          success: function (result) 
          {
            console.log('ajax successed');
          },
          error: function (result) 
          {
            console.log('ajax error');
          }
        })
        .done(resolve)
        .fail(reject);
    });
  }

  function timer_1s() 
  {
    return new Promise(function (resolve, reject) 
    {
      timer2 = setInterval(function () 
      {
        console.log("In the 1s timer function");
        resolve('Time is up');
      }, 1000);
    });
  }

  var p3 = ex_btn_ajax();
  var p4 = timer_1s();
  Promise.all([p3, p4]).then(values => 
  {
    console.log('ex_status = ', ex_status);
    ex_counter++;
    clearInterval(timer2);
    console.log(ex_counter, values);
    //judgment switch sample
    if (ex_counter == timeout_list[0] & ex_status == 0)
    {
      gas_in_flag = true;
    }
    if (stop_timer1 == true & gas_in_flag == false & ex_status == 0) 
    {
      retry_ex_btn_timer1s_promise();
    }
    if (stop_timer1 == false)
    {
      console.log('stop');
    }
    if (gas_in_flag == true)
    {
      console.log('time to switch sample')
      gas_in_ajax_promise();
    }

    //judgment switch purge
    if (ex_counter == timeout_list[1] & ex_status == 1)
    {
      recovery_flag = true;
    }
    if (stop_timer1 == true & recovery_flag == false & ex_status == 1) 
    {
      retry_ex_btn_timer1s_promise();
    }
    if (recovery_flag == true) 
    {
      console.log('its time to recovery');
      recovery_ajax_promise();
    }

    // judgment experiment done
    if (ex_status == 2)
    {
      if(stop_timer1 == true)
      {
        retry_ex_btn_timer1s_promise();
      }
      if(ex_counter == timeout_list[2])
      {
        stop_timer1 == false;
        console.log('Experiment Done');
        stop_btn_func();
        ex_done_ajax_promise();
      }
    }
  });
}

function retry_ex_btn_timer1s_promise() 
{
  ex_btn_timer1s_promise();
}

function ex_done_ajax_promise() 
{
  function ex_done_ajax() 
  {
    return new Promise(function (resolve, reject) 
    {
      var data =
      {
        'btn': 'ex_done',
      }
      $.ajax
        ({
          type: "POST",
          url: "/",
          data: JSON.stringify(data, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          success: function (result) 
          {
            console.log('ajax successed_send_ex_done');
          },
          error: function (result) 
          {
            console.log('ajax error');
          }
        })
        .done(resolve)
        .fail(reject);
    });
  }

  var p7 = ex_done_ajax();
  Promise.all([p7]).then(values => 
  {
    console.log(values);
  });
}