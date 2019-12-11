function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function Calculate(){
    jwt_token = '124'
    data = {
      'jwt': jwt_token,
      'sigma': 0.01,
      'shift': 50,
      'period': 10
    }
    $.ajax({
        url: "/api/api_proxy/add_task/",
        type: "post",
        data: data,
        cache: false,
        success: async function(response){
          console.log(response);
          $("#results").append(response);
         
          var id = response.id;
          console.log(id);
          var is_done = false;
          while(!is_done)
          {
            await sleep(50);
            $.getJSON('/api/api_proxy/progress/?job_id='+id, function(data){
              console.log(data);
                $('#progress').append(data.progress);
                if (parseInt(data.progress) > 90.0) {
                    is_done = true;  
                }
            });
          }
          
        },

        
        
      });
}