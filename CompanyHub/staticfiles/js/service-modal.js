document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll(".enquiry-btn");

    buttons.forEach(function(button){

        button.addEventListener("click", function(){

            const serviceId = this.dataset.serviceId;

            const serviceName = this.dataset.serviceName;

            document.getElementById("selectedService").value = serviceId;

            document.getElementById("selectedServiceName").value = serviceName;

        });

    });

});