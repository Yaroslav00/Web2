
$(document).ready(function(){
    console.log(1);
    $("#signup").submit(function(event){
        console.log(2);
        event.preventDefault();
        var email = $("#emailId").val();
        var password = $("#passwordId").val();
        console.log(email);
        console.log(password);
        signup_data = {
            email:email,
            password: password
        };
        request = $.ajax({
            url: "/api/api_proxy/auth/signup/",
            type: "post",
            data: signup_data
        });
        
        // Callback handler that will be called on success
        request.done(function (response){
            console.log(response.token);
            
            if (response.token != null) {
                
                window.location.replace('calculate.html');
                localStorage.setItem('token', response.token);
                localStorage.setItem('email', response.email);
               
                
                
                
    
            } 
          }
        
        );
    
       
    
    
    });
});
