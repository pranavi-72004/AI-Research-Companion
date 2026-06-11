// =========================
// FEATURE SELECTION
// =========================

function setFeature(feature, element){

    document.getElementById("selectedFeature").value = feature;

    document.querySelectorAll(".feature-card")
    .forEach(card=>{
        card.classList.remove("active");
    });

    element.classList.add("active");

    const uploadBtn =
    document.querySelector(".run-btn");

    const labels = {
        summary:"Generate Summary",
        ideas:"Generate Project Ideas",
        roadmap:"Generate Roadmap",
        gap:"Find Research Gaps",
        review:"Generate Literature Review",
        citation:"Generate Citations"
    };

    uploadBtn.innerHTML =
    labels[feature] || "Generate Insights";
}

// =========================
// DRAG & DROP
// =========================

const dropZone =
document.querySelector(".drop-zone");

const fileInput =
document.querySelector(".drop-zone input");

if(dropZone){

    dropZone.addEventListener(
        "dragover",
        (e)=>{
            e.preventDefault();
            dropZone.style.borderColor="#3b82f6";
            dropZone.style.background=
            "rgba(59,130,246,.08)";
        }
    );

    dropZone.addEventListener(
        "dragleave",
        ()=>{
            dropZone.style.borderColor=
            "rgba(255,255,255,.15)";

            dropZone.style.background=
            "transparent";
        }
    );

    dropZone.addEventListener(
        "drop",
        (e)=>{

            e.preventDefault();

            fileInput.files =
            e.dataTransfer.files;

            const file =
            e.dataTransfer.files[0];

            document.querySelector(
            ".drop-content h3"
            ).innerHTML = file.name;

            dropZone.style.background=
            "transparent";
        }
    );

    fileInput.addEventListener(
        "change",
        ()=>{

            if(fileInput.files.length){

                document.querySelector(
                ".drop-content h3"
                ).innerHTML =
                fileInput.files[0].name;

            }

        }
    );
}

// =========================
// LOADING STATE
// =========================

const uploadForm =
document.querySelector(
'form[action="/upload"]'
);

if(uploadForm){

uploadForm.addEventListener(
"submit",
function(){

const btn =
document.querySelector(".run-btn");

btn.innerHTML = `
<span class="spinner"></span>
Analyzing Paper...
`;

btn.disabled = true;

}
);

}

// =========================
// CHAT LOADING
// =========================

const chatForm =
document.querySelector(
'form[action="/ask"]'
);

if(chatForm){

chatForm.addEventListener(
"submit",
function(){

const btn =
document.querySelector(".chat-btn");

btn.innerHTML =
"Thinking...";

btn.disabled = true;

}
);

}

// =========================
// SCROLL ANIMATION
// =========================

const cards =
document.querySelectorAll(
".feature-card,.glass-card"
);

const observer =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity="1";

entry.target.style.transform=
"translateY(0px)";

}

});

},

{
threshold:0.1
}

);

cards.forEach(card=>{

card.style.opacity="0";
card.style.transform=
"translateY(40px)";
card.style.transition=
"all .8s ease";

observer.observe(card);

});

// =========================
// TYPING EFFECT HERO
// =========================

const hero =
document.querySelector(".hero h1");

if(hero){

const text =
hero.innerText;

hero.innerText="";

let i=0;

function typeWriter(){

if(i < text.length){

hero.innerHTML +=
text.charAt(i);

i++;

setTimeout(
typeWriter,
20
);

}

}

setTimeout(
typeWriter,
300
);

}