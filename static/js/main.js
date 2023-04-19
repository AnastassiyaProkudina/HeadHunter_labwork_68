// объявлены переменные для кнопки добавления опыта
const buttonExperience = document.getElementById('btn-add-experience');
const add_experience = document.getElementById('add_experience');

// объявлены переменные для кнопки добавления образования
const buttonEducation = document.getElementById('btn-add-education');
const add_education = document.getElementById('add_education');

// функция для получения значений из ввода при нажатии кнопки buttonExperience
function getInputValuesExperience() {
    let companyName = document.getElementById('company_name').value;
    let position = document.getElementById('position').value;
    let duties = document.getElementById('duties').value;
    let startedAtExp = document.getElementById('started_at_').value;
    let finishedAtExp = document.getElementById('finished_at_').value;
    const cvID = document.querySelector("#cv_experience");
    let cv_id = parseInt(cvID.dataset.cv)
    return {
        "company_name": companyName,
        "position": position,
        "duties": duties,
        "started_at": startedAtExp,
        "finished_at": finishedAtExp,
        "cv_id": cv_id,
    }
}

// создание карточки для отображения добавленного опыта работы на странице
function createExperienceCard({id, company_name, position, duties, started_at, finished_at}) {
    const cardExp = document.createElement('div');
    cardExp.className = 'card mb-2';
    cardExp.style.width = '20rem';
    cardExp.accessKeyLabel = 'data-education';
    cardExp.accessKey = id

    const cardExpBody = document.createElement('div');
    cardExpBody.className = "card-body";
    cardExp.append(cardExpBody);

    const pPeriod = document.createElement('p');
    pPeriod.className = "card-text";
    pPeriod.innerText = `${started_at} - ${finished_at}`;
    pPeriod.style.color = 'lightblue';
    cardExpBody.append(pPeriod);

    const pCompanyName = document.createElement('p');
    pCompanyName.className = "card-title";
    pCompanyName.innerText = company_name;
    cardExpBody.append(pCompanyName);

    const pPosition = document.createElement('p');
    pPosition.className = "card-text";
    pPosition.innerText = position;
    cardExpBody.append(pPosition);

    const pDuties = document.createElement('p');
    pDuties.className = "card-text";
    pDuties.innerText = duties;
    cardExpBody.append(pDuties);

    add_experience.append(cardExp);
    let educationInput;
    educationInput.name = id;
}

buttonExperience.addEventListener('click', function () {
    let request = new XMLHttpRequest();
    request.onload = function () {
        let data = JSON.parse(this.response);
        createExperienceCard(data);
        let listExperience;
        listExperience.append(data.id);
    }
    let values = getInputValuesExperience();
    request.open('POST', 'http://127.0.0.1:8000/json-experience/');
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify(values));
})

// функция для получения значений из ввода при нажатии кнопки buttonEducation
function getInputValuesEducation() {
    let place = document.getElementById('place').value;
    let course = document.getElementById('course').value;
    let specialization = document.getElementById('specialization').value;
    let startedAt = document.getElementById('started_at').value;
    let finishedAt = document.getElementById('finished_at').value;
    const cvID = document.querySelector("#cv_education");
    let cv_id = parseInt(cvID.dataset.cv)

    return {
        "place": place,
        "course": course,
        "specialization": specialization,
        "started_at": startedAt,
        "finished_at": finishedAt,
        "cv_id": cv_id,
    }
}

// создание карточки для отображения добавленного образования на странице
function createEducationCard({id, place, course, specialization, started_at, finished_at, cv_id}) {
    const cardEdu = document.createElement('div');
    cardEdu.className = `card mb-2 education-card-${id}`;
    cardEdu.style.width = '18rem';
    cardEdu.dataset.education = id

    const cardHeader = document.createElement('div');
    cardHeader.className = 'card-header';
    cardEdu.append(cardHeader);

    const cardCloseButton = document.createElement('button');
    cardCloseButton.className = `btn-close btn-education-close-${cv_id}`;
    cardCloseButton.id = `btn-education-${id}`
    cardHeader.append(cardCloseButton);
    // cardCloseButton.addEventListener('click', function () {
    //     let req = new XMLHttpRequest();
    //     req.onload = function () {
    //         if (this.status === 200) {
    //             cardEdu.style.display = "none";
    //         }
    //     }
    //     req.open('DELETE', `http://127.0.0.1:8000/json-education-delete/${id}`);
    //     req.setRequestHeader('Content-Type', 'application/json');
    //     req.send(JSON.stringify({"pk": education}));
    //
    // })

    const cardEduBody = document.createElement('div');
    cardEduBody.className = "card-body";
    cardEdu.append(cardEduBody);

    const pPeriod = document.createElement('p');
    pPeriod.className = "card-text";
    pPeriod.innerText = `${started_at} - ${finished_at}`;
    pPeriod.style.color = 'lightblue';
    cardEduBody.append(pPeriod);

    const pPlace = document.createElement('p');
    pPlace.className = "card-title";
    pPlace.innerText = `Образовательное учреждение: ${place}`;
    cardEduBody.append(pPlace);

    const pCourse = document.createElement('p');
    pCourse.className = "card-text";
    pCourse.innerText = `Курс/Факультет: ${course}`;
    cardEduBody.append(pCourse);

    const pSpecialization = document.createElement('p');
    pSpecialization.className = "card-text";
    pSpecialization.innerText = `Специальность: ${specialization}`;
    cardEduBody.append(pSpecialization);

    add_education.append(cardEdu);
}

buttonEducation.addEventListener('click', function () {
    let xhr = new XMLHttpRequest();
    xhr.onload = function () {

        let data = JSON.parse(this.response);
        createEducationCard(data)
    }
    let values = getInputValuesEducation();
    xhr.open('POST', `http://127.0.0.1:8000/json-education/`);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.send(JSON.stringify(values));
})


// объявлены переменные для кнопки добавления резюме
const buttonUpdateCV = document.getElementById('btn-add-education');
const add_Update = document.getElementById('add_education');