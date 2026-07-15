const inquiryModal = document.getElementById("inquiryModal");

if (inquiryModal){

    inquiryModal.addEventListener("show.bs.modal", function(event){

        const button = event.relatedTarget;

        const serviceID = button.getAttribute("data-service");

        const serviceTitle = button.getAttribute("data-title");

        document.getElementById("selectedService").innerHTML = serviceTitle;

        document.getElementById("id_service_id").value = serviceID;

    });

}