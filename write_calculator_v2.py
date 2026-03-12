content = '''import { useState, useEffect } from "react";

const fmt = (n) => "$" + Math.round(n).toLocaleString();

export default function CostOfDelayCalculator() {
  const [trucks, setTrucks] = useState(25);
  const [emptyPct, setEmptyPct] = useState(15);
  const [revenuePerTruck, setRevenuePerTruck] = useState(3200);
  const [recruiterHourly, setRecruiterHourly] = useState(22);
  const [recruiterHoursOnBadLeads, setRecruiterHoursOnBadLeads] = useState(3);
  const [timeToHire, setTimeToHire] = useState(18);
  const [revealed, setRevealed] = useState(false);

  const emptyTrucks = Math.round(trucks * (emptyPct / 100));
  const weeklyRevenueLost = emptyTrucks * revenuePerTruck;
  const monthlyRevenueLost = weeklyRevenueLost * 4.33;
  const recruiterWastePerDay = recruiterHourly * recruiterHoursOnBadLeads;
  const recruiterWastePerMonth = recruiterWastePerDay * 22;
  const ssTimeToHire = Math.round(timeToHire * 0.55);
  const daysSaved = timeToHire - ssTimeToHire;
  const revenueFromFasterHire = daysSaved * (revenuePerTruck / 7) * emptyTrucks;
  const totalMonthlyBleed = monthlyRevenueLost + recruiterWastePerMonth;
  const totalAnnualBleed = totalMonthlyBleed * 12;
  const weeklyBleed = totalMonthlyBleed / 4.33;

  useEffect(() => {
    const timer = setTimeout(() => setRevealed(true), 300);
    return () => clearTimeout(timer);
  }, []);

  const Slider = ({ label, value, min, max, step = 1, onChange, prefix = "", suffix = "" }) => (
    <div style={{ marginBottom: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
        <span style={{ fontSize: 13, color: "#94a3b8", fontFamily: "\'DM Sans\', sans-serif", letterSpacing: 0.3 }}>{label}</span>
        <span style={{ fontSize: 15, fontWeight: 700, color: "#FF00CC", fontFamily: "\'DM Mono\', monospace" }}>
          {prefix}{value.toLocaleString()}{suffix}
        </span>
      </div>
      <div style={{ position: "relative", height: 44, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 6, background: "#1e293b", borderRadius: 99 }}>
          <div style={{
            position: "absolute", left: 0, top: 0, height: "100%", borderRadius: 99,
            background: "linear-gradient(90deg, #FF00CC, #ff66e0)",
            width: `${((value - min) / (max - min)) * 100}%`,
            transition: "width 0.15s ease"
          }} />
        </div>
        <div style={{
          position: "absolute",
          left: `calc(${((value - min) / (max - min)) * 100}% - 20px)`,
          transition: "left 0.15s ease",
          width: 40, height: 32,
          background: "#FF00CC",
          borderRadius: 8,
          display: "flex", alignItems: "center", justifyContent: "center",
          gap: 4,
          boxShadow: "0 0 14px #FF00CC99",
          pointerEvents: "none",
          zIndex: 2,
        }}>
          <svg width="8" height="12" viewBox="0 0 7 10" fill="none">
            <path d="M5.5 1L1.5 5L5.5 9" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          <svg width="8" height="12" viewBox="0 0 7 10" fill="none">
            <path d="M1.5 1L5.5 5L1.5 9" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </div>
        <input
          type="range" min={min} max={max} step={step} value={value}
          onChange={e => onChange(Number(e.target.value))}
          style={{
            position: "absolute", inset: 0, width: "100%", height: "100%",
            opacity: 0, cursor: "grab", margin: 0, zIndex: 3,
            touchAction: "none"
          }}
        />
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 4 }}>
        <span style={{ fontSize: 11, color: "#334155" }}>{prefix}{min.toLocaleString()}{suffix}</span>
        <span style={{ fontSize: 11, color: "#334155" }}>{prefix}{max.toLocaleString()}{suffix}</span>
      </div>
    </div>
  );

  return (
    <div style={{
      minHeight: "100vh",
      background: "#020817",
      fontFamily: "\'DM Sans\', sans-serif",
      padding: "40px 20px",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      overflowX: "hidden",
      width: "100%",
    }}>
      <style>{`
        @import url(\'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500;700&family=Syne:wght@700;800&display=swap\');
        html, body { margin: 0; padding: 0; background: #020817; overflow-x: hidden; }
        * { box-sizing: border-box; }
        input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%; background: #FF00CC; cursor: pointer; box-shadow: 0 0 10px #FF00CC88; }
        .stat-card { transition: transform 0.2s ease, box-shadow 0.2s ease; }
        .stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(255,0,204,0.13) !important; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .reveal { animation: fadeUp 0.5s ease forwards; }
        .calc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 900px; width: 100%; align-items: start; }
        .input-panel { background: #0f172a; border: 1px solid #1e293b; border-radius: 16px; padding: 32px; }
        .results-panel { display: flex; flex-direction: column; gap: 16px; }
        .hero-stat { background: #1a0a14; border: 1px solid rgba(255,0,204,0.3); border-radius: 16px; padding: 28px; text-align: center; }
        .monthly-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .breakdown-row { display: flex; justify-content: space-between; margin-bottom: 10px; align-items: center; flex-wrap: wrap; gap: 4px; }
        .cta-button { display: inline-block; background: linear-gradient(135deg, #FF00CC, #cc0099); color: #fff; font-weight: 700; font-size: 14px; padding: 12px 28px; border-radius: 99px; font-family: \'DM Sans\', sans-serif; letter-spacing: 0.5px; text-decoration: none; box-shadow: 0 4px 20px rgba(255,0,204,0.27); }
        @media (max-width: 700px) {
          .calc-grid { grid-template-columns: 1fr; gap: 16px; }
          .input-panel { padding: 20px 16px; }
          .hero-stat { padding: 20px 16px; }
          .cta-button { display: block; text-align: center; padding: 14px 20px; font-size: 15px; }
        }
        @media (max-width: 400px) {
          .monthly-grid { grid-template-columns: 1fr; }
        }
      `}</style>

      <div style={{ textAlign: "center", marginBottom: 40, maxWidth: 600, width: "100%" }}>
        <div style={{
          display: "inline-block", background: "rgba(255,0,204,0.08)", border: "1px solid rgba(255,0,204,0.25)",
          borderRadius: 99, padding: "6px 16px", marginBottom: 16
        }}>
          <span style={{ fontSize: 12, color: "#FF00CC", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1 }}>
            SEATED SELECT // FLEET CALCULATOR
          </span>
        </div>
        <h1 style={{
          fontSize: "clamp(26px, 5vw, 42px)", fontFamily: "\'Syne\', sans-serif",
          fontWeight: 800, color: "#f8fafc", margin: "0 0 12px", lineHeight: 1.1
        }}>
          What Is Your Recruiting<br />
          <span style={{ color: "#FF00CC" }}>Delay Costing You?</span>
        </h1>
        <p style={{ color: "#64748b", fontSize: 15, margin: 0, lineHeight: 1.6 }}>
          Move the sliders to match your fleet. See what slow, unqualified leads are bleeding from your operation every single week.
        </p>
      </div>

      <div className="calc-grid">
        <div className="input-panel">
          <h2 style={{ fontSize: 13, color: "#475569", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1, marginBottom: 28, marginTop: 0 }}>
            YOUR FLEET PROFILE
          </h2>
          <Slider label="Total Power Units" value={trucks} min={10} max={500} step={5} onChange={setTrucks} suffix=" trucks" />
          <Slider label="Average Empty Seats (%)" value={emptyPct} min={5} max={40} onChange={setEmptyPct} suffix="%" />
          <Slider label="Weekly Revenue Per Truck" value={revenuePerTruck} min={1500} max={8000} step={100} onChange={setRevenuePerTruck} prefix="$" />
          <Slider label="Recruiter Hourly Rate" value={recruiterHourly} min={15} max={55} onChange={setRecruiterHourly} prefix="$" suffix="/hr" />
          <Slider label="Hours/Day on Unqualified Leads" value={recruiterHoursOnBadLeads} min={1} max={7} onChange={setRecruiterHoursOnBadLeads} suffix=" hrs" />
          <Slider label="Current Avg Days to Hire" value={timeToHire} min={7} max={45} onChange={setTimeToHire} suffix=" days" />
        </div>

        <div className="results-panel">
          <div className="stat-card reveal hero-stat">
            <div style={{ fontSize: 12, color: "#FF00CC", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1, marginBottom: 8 }}>
              BLEEDING PER WEEK
            </div>
            <div style={{ fontSize: "clamp(36px, 8vw, 52px)", fontWeight: 800, fontFamily: "\'Syne\', sans-serif", color: "#f8fafc", lineHeight: 1 }}>
              {fmt(weeklyBleed)}
            </div>
            <div style={{ fontSize: 12, color: "#64748b", marginTop: 8 }}>revenue loss + recruiter waste</div>
          </div>

          <div className="monthly-grid">
            {[
              { label: "MONTHLY COST", value: fmt(totalMonthlyBleed), sub: "of delay" },
              { label: "ANNUAL COST", value: fmt(totalAnnualBleed), sub: "left on table" },
            ].map(({ label, value, sub }) => (
              <div key={label} className="stat-card" style={{ background: "#0f172a", border: "1px solid #1e293b", borderRadius: 12, padding: 20, textAlign: "center" }}>
                <div style={{ fontSize: 10, color: "#475569", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1, marginBottom: 6 }}>{label}</div>
                <div style={{ fontSize: 22, fontWeight: 700, color: "#f8fafc", fontFamily: "\'Syne\', sans-serif" }}>{value}</div>
                <div style={{ fontSize: 11, color: "#475569", marginTop: 4 }}>{sub}</div>
              </div>
            ))}
          </div>

          <div style={{ background: "#0f172a", border: "1px solid #1e293b", borderRadius: 12, padding: 20 }}>
            <div style={{ fontSize: 11, color: "#475569", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1, marginBottom: 16 }}>BREAKDOWN</div>
            {[
              { label: "Empty trucks (monthly)", value: fmt(monthlyRevenueLost), color: "#f87171" },
              { label: "Recruiter waste (monthly)", value: fmt(recruiterWastePerMonth), color: "#fb923c" },
              { label: "Days saved w/ Seated Select", value: `${daysSaved} days`, color: "#34d399" },
              { label: "Revenue unlocked (faster hire)", value: fmt(revenueFromFasterHire), color: "#34d399" },
            ].map(({ label, value, color }) => (
              <div key={label} className="breakdown-row">
                <span style={{ fontSize: 13, color: "#64748b" }}>{label}</span>
                <span style={{ fontSize: 14, fontWeight: 700, color, fontFamily: "\'DM Mono\', monospace" }}>{value}</span>
              </div>
            ))}
          </div>

          <div style={{ background: "#061410", border: "1px solid rgba(22,163,74,0.25)", borderRadius: 12, padding: 20 }}>
            <div style={{ fontSize: 11, color: "#16a34a", fontFamily: "\'DM Mono\', monospace", letterSpacing: 1, marginBottom: 12 }}>WITH SEATED SELECT</div>
            <div style={{ fontSize: 13, color: "#86efac", lineHeight: 1.7 }}>
              Pre-qualified drivers arrive with a quality score before your recruiter answers the phone. Your team stops chasing and starts selecting.
            </div>
            <div style={{ marginTop: 16, paddingTop: 16, borderTop: "1px solid rgba(22,163,74,0.12)" }}>
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                <span style={{ fontSize: 12, color: "#4ade80" }}>Est. time-to-hire with SS</span>
                <span style={{ fontSize: 14, fontWeight: 700, color: "#4ade80", fontFamily: "\'DM Mono\', monospace" }}>{ssTimeToHire} days</span>
              </div>
            </div>
          </div>

          <div style={{ textAlign: "center", paddingTop: 4 }}>
            <div style={{ fontSize: 12, color: "#475569", marginBottom: 10 }}>Ready to stop the bleed?</div>
            <a href="https://calendly.com/seated-social/30min" target="_blank" rel="noopener noreferrer" className="cta-button">
              Get a Seated Select Demo
            </a>
            <div style={{ fontSize: 11, color: "#334155", marginTop: 10 }}>seatedselect.com</div>
          </div>
        </div>
      </div>
    </div>
  );
}
'''

with open("src/CostOfDelayCalculator.jsx", "w") as f:
    f.write(content)
print("File written successfully")
