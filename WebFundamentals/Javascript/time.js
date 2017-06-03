
        var HOUR = 8;
        var MINUTE = 20;
        var PERIOD = "AM";
        var TIME = HOUR + MINUTE + COLON + PERIOD;
        var COLON = ":";

        if (MINUTE > 30 && PERIOD === "AM"){
            HOUR++;
            console.log("It's almost", HOUR, "in the morning!");
        } 
        if (MINUTE < 30 && PERIOD === "AM"){
            console.log("It's just after", HOUR, "in the morning.");
        }
        if (MINUTE < 30 && PERIOD !== "AM"){
            console.log("It's just after", HOUR, "in the evening.");
        }
