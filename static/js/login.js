
$(document).ready(function(){
    
    $("#login").submit(function(event){
        event.preventDefault();
        var email = $("#emailId").val();
        var password = $("#passwordId").val();
        
        login_data = {
            email:email,
            password: password
        };
        request = $.ajax({
            url: "/api/api_proxy/auth/login/",
            type: "post",
            data: login_data
        });
        
        // Callback handler that will be called on success
        request.done(function (response){
            console.log(response.token);
            
            if (response.token != null) {
                
                window.location.replace('calculate.html');
                localStorage.setItem('token', response.token);
                
                
                
                
    
            } 
          }
        
        );
    
       
    
    
    });
});
