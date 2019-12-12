function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function Calculate(){
    event.preventDefault();
    $('#taskProgress').attr("value", 0);
    $('#progress').html(0);
    jwt_token = localStorage.getItem("token")
    data = {
      'jwt': jwt_token,
      'sigma': $("#sigma").val(),
      'shift': $("#shift").val(),
      'period': $("#period").val()
    }
    $("#sigma").val("");
    $("#shift").val("");
    $("#period").val("");
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
          var current_progress = 0;
          while(!is_done)
          {
            if (parseInt(current_progress) > 94.0) {
              is_done = true;  
            }
            await sleep(50);
            if(!is_done)
            {
              $.getJSON('/api/api_proxy/progress/?job_id='+id, function(data){
                console.log(data);
                current_progress = parseInt(data.progress);
                $('#taskProgress').attr("value", data.progress);
                $('#progress').html(data.progress);
                if (parseInt(data.progress) > 99.0) {
                    is_done = true;  
                }
            });
            }
            
          }
          
        },

        
        
      });
};