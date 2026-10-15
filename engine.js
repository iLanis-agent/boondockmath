var BoondockMath = (function () {
  function num(x) { return typeof x === "number" && isFinite(x); }
  function pos(x) { return num(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function jsnum(x) { if (typeof x === "number" && isFinite(x) && x === Math.trunc(x)) return String(Math.trunc(x)); return String(x); }
  var GRAY_PER_PERSON = 4, HOURS_PER_BOTTLE = 12;
  function tankPlan(grayGal, people) {
    if (!pos(grayGal)) return { error: "the gray tank gallons must be above zero" };
    if (!pos(people)) return { error: "the headcount must be above zero" };
    var days = grayGal / (people * GRAY_PER_PERSON);
    var verdict = days < 3 ? "the gray tank ends the weekend early"
      : days <= 5 ? "a working week at most"
      : "the tank outlasts the fresh water";
    return { days: r1(days), verdict: verdict };
  }
  function renderTank(r, grayGal, people) {
    var word = people === 1 ? " person aboard" : " people aboard";
    return "The " + jsnum(grayGal) + "-gallon gray tank with " + jsnum(people) + word
      + " at the 4-gallon navy-shower norm fills in about " + jsnum(r.days) + " days - " + r.verdict + ".";
  }
  function battPlan(bankAh, usablePct, dailyAh) {
    if (!pos(bankAh)) return { error: "the bank amp-hours must be above zero" };
    if (!pos(usablePct) || usablePct > 100) return { error: "the usable percent must sit between zero and 100" };
    if (!pos(dailyAh)) return { error: "the daily amp-hours must be above zero" };
    var usable = bankAh * usablePct / 100;
    var nights = usable / dailyAh;
    var verdict = nights < 1 ? "the lights dim before dawn"
      : nights <= 3 ? "a few honest nights"
      : "the bank outlasts the water";
    return { usable: r1(usable), nights: r1(nights), verdict: verdict };
  }
  function renderBatt(r, bankAh, usablePct, dailyAh) {
    return "The " + jsnum(bankAh) + " amp-hour bank honestly gives " + jsnum(usablePct) + "% of itself - "
      + jsnum(r.usable) + " amp-hours against the " + jsnum(dailyAh) + "-amp-hour day, about " + jsnum(r.nights)
      + " nights - " + r.verdict + ".";
  }
  function propPlan(bottles, hoursPerNight) {
    if (!pos(bottles)) return { error: "the bottle count must be above zero" };
    if (!pos(hoursPerNight)) return { error: "the furnace hours per night must be above zero" };
    var furnaceHours = bottles * HOURS_PER_BOTTLE;
    var nights = furnaceHours / hoursPerNight;
    var verdict = nights < 3 ? "a cold weekend at best"
      : nights <= 7 ? "several honest nights"
      : "the bottles outlast the trip";
    return { furnaceHours: r1(furnaceHours), nights: r1(nights), verdict: verdict };
  }
  function renderProp(r, bottles, hoursPerNight) {
    var word = bottles === 1 ? " bottle holds" : " bottles hold";
    return "The " + jsnum(bottles) + word + " about " + jsnum(r.furnaceHours) + " honest furnace-hours; at "
      + jsnum(hoursPerNight) + " hours a night that is about " + jsnum(r.nights) + " nights - " + r.verdict + ".";
  }
  return { tankPlan: tankPlan, renderTank: renderTank, battPlan: battPlan, renderBatt: renderBatt, propPlan: propPlan, renderProp: renderProp };
})();
if (typeof module !== "undefined" && module.exports) module.exports = BoondockMath;
