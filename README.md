* https://harrypotter-relationships.herokuapp.com/

<p dir="rtl">
<h1 dir="rtl"><strong><span style="text-decoration:underline;">הארי פוטר - רשת חברתית</span></strong></p></h1>


<p dir="rtl">
<h2 dir="rtl"><strong><span style="text-decoration:underline;">מטרת הפרויקט:</span></strong></p></h2>


<p dir="rtl">רשת חברתית של הארי פוטר אשר מגדירה את טיב מערכת היחסים בין כל הדמויות. הניתוח נעשה עבור כל ספר, והתוצאה הסופית הינה ממוצע משוקלל של הנתונים.</p>

<p dir="rtl">
<h2 dir="rtl"><strong><span style="text-decoration:underline;">הקשר למדעי הרוח הדיגיטליים:</span></strong></p></h2>


<p dir="rtl">
בפרויקט זה אנו משתמשים בידע התכנותי שצברנו על מנת לתכנן אלגוריתמים שיבצעו ניתוח ועיבוד מידע בפלטפורמות דיגיטליות תוך כדי שילוב העניין והידע שלנו בסדרת הספרים הנוכחית.</p>

<p dir="rtl">
<h2 dir="rtl"><strong><span style="text-decoration:underline;">כלים - שפות פיתוח:</span></strong></p></h2>

* Python 
* Javascript
* HTML
* CSS
* REACT
* SigmaJS

<p dir="rtl">
<h2 dir="rtl"><strong><span style="text-decoration:underline;">תוכנית עבודה:</span></strong></p></h2>

<p dir="rtl">
  
<h3><strong><span style="text-decoration:underline;">backend:</span></strong></p></h3>



  
יצירת המחלקות הבאות: </p>
<strong> Book - <p/> </strong>
מקבלת קובץ txt המהווה את הספר ה- i, ושומרת את כל המילים המורכבות מאותיות באנגלית.</p>
<strong> Character - <p/> </strong>
מקבלת שם של דמות ויוצרת אובייקט שמייצג את הדמות ומכיל את השדות הבאים: </p>
* שם
* כינויים (alias)
* מילון אשר המפתח שלו הוא מספר הספר והערך שלו הוא רשימה שכל איבר בה מייצג מופע של הדמות והוא המילה ה- i בספר
* מילון אשר המפתח שלו הוא דמות (לא כולל הדמות הנוכחית) והערך הוא מערך בגודל 7 אשר כל תא בערך מייצג את הקשר שאנחנו מנסים לכמת בפרויקט הזה בין הדמות הנוכחית לשאר הדמויות עבור כל ספר.</p>

<strong> Relationship - <p/> </strong>

מקבלת דמות (viewpoint), בעלת שדה 'מילון' אשר המפתח הוא כל אחת מהדמויות השונות מהדמות viewpoint והערך הוא הממוצע המשוקלל של היחסים עם הדמות הנוכחית והדמות viewpoint המעודכן ע"י המחלקה CharacterRelationships.
<p/>
<strong> CharacterRelationships - <p/></strong>
מכילה שתי פונקציות סטטיות: </p>

* פונקציה משנית אשר מחשבת את הממוצע המשוקלל.
* הפונקציה הראשית מקבלת דמות שנסמן כ- source ודמות שנסמן כ- target, עוברת על כל אחד מהמופעים של הדמות source ובודקת האם הדמות target מופיעה במרחק של לכל היותר הקבוע שהגדרנו. </p> 

את התוצאות אנחנו שומרים בקובץ Json בשם results אשר כל אובייקט המפתח הוא דמות source והערך הוא רשימה של כל שאר הדמויות עם הממוצע המשוקלל
.</p>
  
<h3><strong><span style="text-decoration:underline;">frontend:</span></strong></p></h3>


הצגת קובץ ה- results בצורה גרפית: </p>

שימוש בסרגל כלים מצד שמאל אשר מכיל את כל אחת מהדמויות בספר- כאשר נלחץ על דמות מסוימת נקבל גרף שבמרכזו קודקוד בצבע אדום המהווה את הדמות שעליה לחצנו, וקשת ב
בגרף היא מהקודקוד המרכזי לכל קודקוד כחול המייצג דמות אשר הממוצע המשוקלל שלה עם הדמות הנוכחית גדול מאפס (קיימת מערכת יחסים כפי שהגדרנו בין שתי הדמויות).<p> הגודל של הקודקוד מעיד על מידת הקשר בין שתי הדמויות.
</p>

מקורות:

Books- https://github.com/CorentinMAG/TEXT_MINING_HP
Characters - https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters
