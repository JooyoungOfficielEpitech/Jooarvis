document.addEventListener("DOMContentLoaded", () => {
    const calendarEl = document.getElementById("calendar");

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        headerToolbar: {
            left: "prev,next today",
            center: "title",
            right: "dayGridMonth,dayGridWeek,dayGridDay",
        },
        editable: true, // Drag & Drop 활성화
        selectable: true, // 날짜 선택 활성화
        eventLongPressDelay: 50, // 터치 & 드래그 활성화 (기본값: 1000ms)
        dragScroll: true, // 터치 시 화면 스크롤 허용
        events: async function(fetchInfo, successCallback, failureCallback) {
            try {
                const response = await fetch("http://127.0.0.1:8000/api/schedules");
                const events = await response.json();
                successCallback(events);
            } catch (error) {
                console.error("Error fetching events:", error);
                failureCallback(error);
            }
        },
        eventDrop: async function(info) {
            const updatedEvent = {
                id: info.event.id,
                start: info.event.startStr,
                end: info.event.endStr
            };
            try {
                await fetch(`http://127.0.0.1:8000/api/schedules/${info.event.id}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(updatedEvent),
                });
                alert("Event updated!");
            } catch (error) {
                console.error("Error updating event:", error);
            }
        },
    });

    calendar.render();
});
