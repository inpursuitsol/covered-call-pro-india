CoveredCall Pro India — Project Memory (26 Jun 2026)
Vision

CoveredCall Pro India is not another option chain viewer.

It is a professional decision-support platform for covered call writing on Indian indices.

Primary objective:

Generate consistent monthly income while protecting long-term holdings.

The first implementation is focused on NIFTY covered calls.

Future expansion:

Bank NIFTY
FINNIFTY
Sensex
Individual stocks
Broker integration
Automation
Long-term Goal

This project is intended to become my daily trading platform for life, not a demo or tutorial project.

Every design decision should optimize for:

maintainability
modularity
readability
professional architecture
scalability

Never take shortcuts that create technical debt.

My Trading Profile

Current profile:

NIFTY BeES: 1200 units
Covered Call Lots: 5
Preferred OTM: 2.5%
Strike interval: Always 100-point strikes
Minimum VIX: configurable
Paper Trading: enabled initially

Nothing above should be hardcoded.

Everything belongs in settings/profile.

Important Design Principles
Never hardcode values.

Any value that may change later belongs in:

settings.json
profile
service
provider
calculation

Never inside dashboard logic.

Dashboard should never contain business logic.

Dashboard should simply ask:

ATHENA, what should I do today?

Everything else happens behind the scenes.

ATHENA must explain recommendations.

Not:

Sell 24700 CE

Instead:

Sell 24700 CE because:

Best premium
Good distance
Acceptable VIX
Highest probability
Highest overall score

ATHENA should always explain itself.

Current Folder Structure
covered-call-pro-india/

app.py

README.md

PROJECT.md

requirements.txt

.gitignore

assets/

core/
    config.py

data/
    settings.json

docs/

models/
    recommendation.py
    trade_recommendation.py
    user_profile.py

pages/

services/

    providers/
        athena_engine.py

    expiry_service.py

    live_market.py

    market_service.py

    profile_service.py

    recommendation_service.py

    settings_service.py

    strategy_service.py

    strike_selector.py

tests/

utils/

Future recommendation:

Move providers outside services.

providers/
    athena_engine.py
    market_provider.py
    option_chain_provider.py
Completed Modules
Live Market

Gets:

NIFTY price
India VIX (placeholder/fallback if unavailable)
Expiry Service

Returns next expiry.

Market Service

Returns snapshot including:

NIFTY
VIX
Opportunity Score
Risk
Expected Income
Expiry
Last Updated
Settings Service

Reads settings.json.

No hardcoded trading preferences.

Profile Service

Converts settings into UserProfile dataclass.

Works correctly.

Bug fixed:

profile_service = ProfileService()

NOT

profile_service = ProfileService
Strike Selector

Uses:

spot

preferred_otm

vix

days_to_expiry

Returns nearest 100 strike.

Example:

24056

↓

24657

↓

24700

Only 100-point strikes.

Recommendation Service

Calls ATHENA.

Dashboard should only use Recommendation Service.

Dashboard

Dashboard now shows

Opportunity Score
Market Mood
Risk
Expected Income
Live NIFTY

ATHENA recommendation card

Information card

Uses services.

Almost no hardcoded values remain.

Architecture
Dashboard

↓

Recommendation Service

↓

ATHENA Engine

↓

Market Service

↓

Providers

↓

Live Market
Expiry
Profile
Settings

Business logic never belongs inside app.py.

ATHENA Philosophy

ATHENA should think like an experienced covered call trader.

Not like a scanner.

Questions ATHENA should answer:

Should I trade today?

Should I skip?

Should I wait?

Which strike?

Why?

Is premium sufficient?

Is VIX acceptable?

Does it meet income target?

Planned Decision Flow
Live Market

↓

Option Chain

↓

Candidate Generator

↓

Trade Filter

↓

Score Engine

↓

Recommendation

↓

Dashboard
Score Engine

Current idea:

Premium

35%

Distance

20%

VIX

20%

Liquidity

15%

Expiry

10%

Later configurable from settings.

Planned Modules

candidate_service.py

Generates candidate strikes.

Example

24600

24700

24800

trade_filter.py

Rejects strikes because of:

Premium

Liquidity

OI

Spread

Low VIX

Poor yield

option_chain_service.py

Gets:

Expiry

Calls

Puts

Premium

OI

IV

Volume

option_chain_provider.py

Eventually replace Yahoo.

Need reliable NSE-compatible provider.

premium_analyzer.py

Calculates

Expected monthly income

Annualized yield

Return on capital

score_engine.py

Scores every candidate.

ATHENA chooses highest score.

Future Settings

Need to move into settings.json

weights

minimum_monthly_income

premium_target

distance_weights

confidence_weights

risk_weights

Nothing should remain hardcoded.

Ultimate Goal

ATHENA should evaluate every possible covered call and finally say something like:

24700 CE

Confidence 93%

Expected Income ₹18,420

Premium ₹167

Yield 1.18%

Probability OTM 82%

Reason

Highest premium while satisfying

minimum VIX

minimum yield

preferred OTM

risk rules

Recommended.
My Instructions to Future ChatGPT

Continue from this exact architecture.

Do NOT simplify the project.

Do NOT convert it into a beginner tutorial.

Keep everything modular and professionally engineered.

Challenge poor architecture.

Suggest improvements.

Think like a software architect and an experienced Indian options trader.

Every module should be reusable.

Always optimize for a codebase that will still be maintainable 5–10 years from now.
 

