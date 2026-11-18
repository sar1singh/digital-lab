/**
 * Canonical procedural 2D SVG puppet engine for Eddy Owl (@wethinklate).
 * Preserves V1's tall curved-tuft owl head + warm #F59E0B amber owl beak,
 * upgraded with smooth Bezier limb/brow interpolation, word-level lip articulation,
 * self-debate persona color variation (`host` white vs `questioner` pastel sky-blue),
 * and classic 2D cartoon overhead props (lightbulb, storm cloud, question marks, shock, sparkles).
 *
 * Pure function of timeline time `t` so HyperFrames multi-worker capture is deterministic.
 */
(function (global) {
  "use strict";

  const INK = "#141619";
  const HAND_FILL = "#141619";

  const clamp01 = (v) => (v < 0 ? 0 : v > 1 ? 1 : v);
  const lerp = (a, b, t) => a + (b - a) * t;

  function parseHex(hex) {
    const h = hex.replace("#", "");
    return [
      parseInt(h.slice(0, 2), 16),
      parseInt(h.slice(2, 4), 16),
      parseInt(h.slice(4, 6), 16),
    ];
  }

  function lerpHex(hexA, hexB, k) {
    const t = clamp01(k);
    const a = parseHex(hexA);
    const b = parseHex(hexB);
    return (
      "rgb(" +
      Math.round(lerp(a[0], b[0], t)) +
      "," +
      Math.round(lerp(a[1], b[1], t)) +
      "," +
      Math.round(lerp(a[2], b[2], t)) +
      ")"
    );
  }

  function easeOutBack(t, overshoot) {
    const s = overshoot === undefined ? 1.35 : overshoot;
    const x = clamp01(t) - 1;
    return 1 + (s + 1) * x * x * x + s * x * x;
  }

  function easeInOutCubic(t) {
    const x = clamp01(t);
    return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  }

  // Distinct color & styling for Main Narrator vs Skeptic/Questioner Persona
  const PERSONAS = {
    host: {
      headFill: "#FFFFFF",
      celFill: "#E6E1D6",
      beakFill: "#F59E0B",
      collarFill: "#9A4D2A",
      medallionFill: "#C5A059",
      glassesHue: "#141619",
    },
    questioner: {
      headFill: "#DBEAFE",
      celFill: "#93C5FD",
      beakFill: "#F59E0B",
      collarFill: "#1E3A8A",
      medallionFill: "#38BDF8",
      glassesHue: "#1E3A8A",
    },
  };

  // Coordinates centered in x=178 (head 118..238, collar 214, feet 410) matching V1 Owl proportions
  const POSES = {
    CURIOUS: {
      headRot: -6,
      headX: 0,
      headY: 0,
      torsoLean: 175,
      scaleX: 1,
      scaleY: 1,
      browLY: 103,
      browLAngle: -6,
      browRY: 103,
      browRAngle: 4,
      lidTop: 0.0,
      lidBot: 0.0,
      pupilX: -3,
      pupilY: 1,
      pupilR: 5.2,
      jawBase: 0,
      lArmCP: [122, 270],
      lArmEnd: [146, 304],
      lHand: "hip",
      lHandRot: 18,
      rArmCP: [226, 226],
      rArmEnd: [190, 182],
      rHand: "chin",
      rHandRot: -20,
      lKnee: [158, 365],
      lFoot: [146, 410],
      rKnee: [200, 365],
      rFoot: [212, 410],
      tremor: false,
    },
    SKEPTIC_ASK: {
      headRot: 5,
      headX: -4,
      headY: -2,
      torsoLean: 170,
      scaleX: 1.01,
      scaleY: 1.0,
      browLY: 98,
      browLAngle: -14,
      browRY: 106,
      browRAngle: -4,
      lidTop: 0.08,
      lidBot: 0.04,
      pupilX: -4,
      pupilY: -1,
      pupilR: 5.2,
      jawBase: 0,
      lArmCP: [110, 238],
      lArmEnd: [66, 248],
      lHand: "open_spread",
      lHandRot: 195,
      rArmCP: [226, 268],
      rArmEnd: [208, 306],
      rHand: "hip",
      rHandRot: 165,
      lKnee: [154, 366],
      lFoot: [140, 410],
      rKnee: [204, 366],
      rFoot: [216, 410],
      tremor: false,
    },
    PUZZLED: {
      headRot: -11,
      headX: 0,
      headY: 2,
      torsoLean: 180,
      scaleX: 1,
      scaleY: 1,
      browLY: 105,
      browLAngle: 4,
      browRY: 94,
      browRAngle: -16,
      lidTop: 0.12,
      lidBot: 0.06,
      pupilX: -2,
      pupilY: -2,
      pupilR: 5.0,
      jawBase: 0,
      lArmCP: [132, 278],
      lArmEnd: [136, 320],
      lHand: "relaxed",
      lHandRot: 12,
      rArmCP: [256, 194],
      rArmEnd: [236, 92],
      rHand: "scratch",
      rHandRot: -110,
      lKnee: [164, 365],
      lFoot: [154, 410],
      rKnee: [196, 365],
      rFoot: [206, 410],
      tremor: false,
    },
    FURIOUS_POINTING: {
      headRot: 5,
      headX: -6,
      headY: 4,
      torsoLean: 168,
      scaleX: 1.02,
      scaleY: 0.98,
      browLY: 102,
      browLAngle: 22,
      browRY: 102,
      browRAngle: -22,
      lidTop: 0.0,
      lidBot: 0.0,
      pupilX: -5,
      pupilY: 1,
      pupilR: 4.8,
      jawBase: 0.12,
      lArmCP: [108, 224],
      lArmEnd: [48, 200],
      lHand: "point_left",
      lHandRot: 185,
      rArmCP: [226, 272],
      rArmEnd: [204, 306],
      rHand: "hip",
      rHandRot: 165,
      lKnee: [148, 366],
      lFoot: [132, 410],
      rKnee: [212, 366],
      rFoot: [228, 410],
      tremor: false,
    },
    SCHEMING: {
      headRot: 7,
      headX: -4,
      headY: 8,
      torsoLean: 166,
      scaleX: 1.02,
      scaleY: 0.96,
      browLY: 106,
      browLAngle: 20,
      browRY: 106,
      browRAngle: -20,
      lidTop: 0.34,
      lidBot: 0.14,
      pupilX: -4,
      pupilY: 1,
      pupilR: 4.6,
      jawBase: 0,
      lArmCP: [140, 276],
      lArmEnd: [168, 272],
      lHand: "fist",
      lHandRot: 15,
      rArmCP: [212, 276],
      rArmEnd: [184, 272],
      rHand: "fist",
      rHandRot: 165,
      lKnee: [152, 360],
      lFoot: [148, 410],
      rKnee: [206, 360],
      rFoot: [210, 410],
      tremor: false,
    },
    SHOCKED: {
      headRot: -4,
      headX: 2,
      headY: -6,
      torsoLean: 180,
      scaleX: 0.98,
      scaleY: 1.03,
      browLY: 92,
      browLAngle: -14,
      browRY: 92,
      browRAngle: 14,
      lidTop: 0.0,
      lidBot: 0.0,
      pupilX: -2,
      pupilY: 0,
      pupilR: 4.1,
      jawBase: 0.25,
      lArmCP: [122, 250],
      lArmEnd: [84, 282],
      lHand: "open_spread",
      lHandRot: 215,
      rArmCP: [238, 248],
      rArmEnd: [274, 282],
      rHand: "open_spread",
      rHandRot: -35,
      lKnee: [146, 368],
      lFoot: [134, 410],
      rKnee: [212, 368],
      rFoot: [224, 410],
      tremor: false,
    },
    TERRIFIED: {
      headRot: 0,
      headX: 0,
      headY: 4,
      torsoLean: 176,
      scaleX: 1.01,
      scaleY: 0.98,
      browLY: 93,
      browLAngle: -16,
      browRY: 93,
      browRAngle: 16,
      lidTop: 0.0,
      lidBot: 0.0,
      pupilX: 0,
      pupilY: 2,
      pupilR: 3.9,
      jawBase: 0.35,
      lArmCP: [96, 204],
      lArmEnd: [122, 154],
      lHand: "open_spread",
      lHandRot: -85,
      rArmCP: [260, 204],
      rArmEnd: [234, 154],
      rHand: "open_spread",
      rHandRot: -95,
      lKnee: [154, 365],
      lFoot: [136, 410],
      rKnee: [206, 365],
      rFoot: [224, 410],
      tremor: true,
    },
    SMUG: {
      headRot: 4,
      headX: 0,
      headY: 2,
      torsoLean: 178,
      scaleX: 1,
      scaleY: 1,
      browLY: 106,
      browLAngle: 8,
      browRY: 106,
      browRAngle: -8,
      lidTop: 0.38,
      lidBot: 0.0,
      pupilX: -3,
      pupilY: 0,
      pupilR: 5.0,
      jawBase: 0,
      lArmCP: [128, 274],
      lArmEnd: [212, 274],
      lHand: "folded",
      lHandRot: 0,
      rArmCP: [228, 274],
      rArmEnd: [144, 274],
      rHand: "folded",
      rHandRot: 180,
      lKnee: [158, 365],
      lFoot: [146, 410],
      rKnee: [198, 365],
      rFoot: [210, 410],
      tremor: false,
    },
  };

  function handMarkup(kind) {
    if (kind === "point_left" || kind === "point") {
      return '<path d="M-4,-5 L16,-2 C19,-2 19,3 15,3 L4,3 C6,7 2,11 -4,9 C-9,7 -9,-3 -4,-5 Z" fill="' + HAND_FILL + '"/>';
    }
    if (kind === "open_spread") {
      return '<path d="M-4,6 L-8,-8 M0,6 L0,-11 M4,6 L8,-9 M7,7 L13,-2 M-6,6 C-6,12 6,12 6,6 Z" fill="' + HAND_FILL + '" stroke="' + HAND_FILL + '" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>';
    }
    if (kind === "scratch") {
      return '<path d="M-3,4 L-7,-9 M1,4 L2,-11 M5,4 L9,-7 M-5,5 C-5,10 6,10 6,4 Z" fill="' + HAND_FILL + '" stroke="' + HAND_FILL + '" stroke-width="3.0" stroke-linecap="round"/>';
    }
    if (kind === "folded") {
      return '<circle cx="0" cy="0" r="3.2" fill="' + HAND_FILL + '"/>';
    }
    return '<ellipse cx="0" cy="0" rx="6.0" ry="5.0" fill="' + HAND_FILL + '"/>';
  }

  function emoteMarkup(kind) {
    if (kind === "lightbulb") {
      return (
        '<g transform="translate(178, 4)">' +
        '<path d="M0,-38 L0,-50 M-26,-28 L-36,-38 M26,-28 L36,-38 M-38,-6 L-50,-8 M38,-6 L50,-8" stroke="#F59E0B" stroke-width="4.5" stroke-linecap="round"/>' +
        '<path d="M-19,-8 C-21,-24 -11,-34 0,-34 C11,-34 21,-24 19,-8 C18,1 11,6 10,13 L-10,13 C-11,6 -18,1 -19,-8 Z" fill="#FEF08A" stroke="' + INK + '" stroke-width="4" stroke-linejoin="round"/>' +
        '<path d="M-5,2 L-3,-8 L0,-3 L3,-8 L5,2" fill="none" stroke="#B45309" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>' +
        '<rect x="-8" y="13" width="16" height="9" rx="2" fill="#94A3B8" stroke="' + INK + '" stroke-width="3.2"/>' +
        '<line x1="-6" y1="26" x2="6" y2="26" stroke="' + INK + '" stroke-width="3.5" stroke-linecap="round"/>' +
        "</g>"
      );
    }
    if (kind === "storm_cloud") {
      return (
        '<g transform="translate(178, 6)">' +
        '<path d="M-48,4 C-56,4 -60,-8 -50,-14 C-50,-28 -34,-34 -24,-26 C-16,-40 8,-40 16,-24 C30,-28 46,-18 42,-4 C52,-2 52,12 40,12 L-42,12 C-52,12 -52,6 -48,4 Z" fill="#94A3B8" stroke="' + INK + '" stroke-width="4.2" stroke-linejoin="round"/>' +
        '<path d="M-4,12 L-14,27 L-2,27 L-10,44 L10,22 L-1,22 L7,12 Z" fill="#FACC15" stroke="' + INK + '" stroke-width="2.6" stroke-linejoin="round"/>' +
        '<path d="M-32,20 L-36,30 M24,20 L20,30" stroke="#60A5FA" stroke-width="3.4" stroke-linecap="round"/>' +
        "</g>"
      );
    }
    if (kind === "questions") {
      return (
        "<g>" +
        '<text x="72" y="42" transform="rotate(-14 72 42)" font-family="Montserrat" font-weight="900" font-size="44" fill="#1D4ED8" stroke="#FFFFFF" stroke-width="5" paint-order="stroke">?</text>' +
        '<text x="166" y="16" font-family="Montserrat" font-weight="900" font-size="56" fill="#D92D20" stroke="#FFFFFF" stroke-width="5" paint-order="stroke">?</text>' +
        '<text x="260" y="46" transform="rotate(14 260 46)" font-family="Montserrat" font-weight="900" font-size="46" fill="' + INK + '" stroke="#FFFFFF" stroke-width="5" paint-order="stroke">?</text>' +
        "</g>"
      );
    }
    if (kind === "shock_burst") {
      return (
        "<g>" +
        '<text x="262" y="68" font-family="Montserrat" font-weight="900" font-size="60" fill="#D92D20" stroke="#FFFFFF" stroke-width="5" paint-order="stroke">!</text>' +
        '<path d="M258,92 L284,84 M262,108 L288,112 M96,82 L74,74" stroke="' + INK + '" stroke-width="4.2" stroke-linecap="round"/>' +
        '<path d="M98,100 C90,106 90,114 96,114 C102,114 102,106 98,100 Z" fill="#60A5FA" stroke="' + INK + '" stroke-width="2.8"/>' +
        "</g>"
      );
    }
    if (kind === "sparkles") {
      return (
        "<g>" +
        '<path d="M84,38 L88,52 L102,56 L88,60 L84,74 L80,60 L66,56 L80,52 Z" fill="#FACC15" stroke="' + INK + '" stroke-width="2.8" stroke-linejoin="round"/>' +
        '<path d="M268,42 L272,54 L284,58 L272,62 L268,74 L264,62 L252,58 L264,54 Z" fill="#FACC15" stroke="' + INK + '" stroke-width="2.8" stroke-linejoin="round"/>' +
        '<path d="M178,10 L181,19 L190,22 L181,25 L178,34 L175,25 L166,22 L175,19 Z" fill="#FACC15" stroke="' + INK + '" stroke-width="2.4" stroke-linejoin="round"/>' +
        "</g>"
      );
    }
    return "";
  }

  function interpVec2(a, b, k) {
    return [lerp(a[0], b[0], k), lerp(a[1], b[1], k)];
  }

  function createEddyRig(opts) {
    const container = opts.container;
    const prefix = opts.prefix || "eddy";
    const darkGround = !!opts.darkGround;
    const talkWindows = opts.talkWindows || [];
    const wordWindows = opts.wordWindows || [];
    const keyframes = opts.keyframes || [{ at: 0, pose: "CURIOUS", dur: 0.35 }];
    const personas = opts.personas || [{ at: 0, role: "host", dur: 0.25 }];
    const emotes = opts.emotes || [];
    const lookTargets = opts.lookTargets || [];

    const backdropMarkup = darkGround
      ? '<circle cx="178" cy="242" r="186" fill="#F4EFE6" stroke="rgba(255,255,255,0.28)" stroke-width="5"/>' +
        '<circle cx="178" cy="242" r="174" fill="none" stroke="rgba(17,19,24,0.08)" stroke-width="2" stroke-dasharray="6 8"/>'
      : "";

    container.innerHTML =
      '<svg viewBox="0 -44 360 484" width="100%" height="100%" style="overflow:visible">' +
      "<defs>" +
      '<clipPath id="' + prefix + '-eyeL-clip"><circle cx="152" cy="134" r="22.5"/></clipPath>' +
      '<clipPath id="' + prefix + '-eyeR-clip"><circle cx="204" cy="134" r="22.5"/></clipPath>' +
      '<filter id="' + prefix + '-boil" x="-8%" y="-8%" width="116%" height="116%">' +
      '<feTurbulence id="' + prefix + '-turb" type="fractalNoise" baseFrequency="0.028" numOctaves="2" seed="1" result="n"/>' +
      '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.1"/>' +
      "</filter>" +
      "</defs>" +
      backdropMarkup +
      '<ellipse id="' + prefix + '-shadow" cx="178" cy="414" rx="70" ry="11" fill="rgba(17,19,24,0.14)"/>' +
      '<g id="' + prefix + '-whole" filter="url(#' + prefix + '-boil)">' +
      '<path id="' + prefix + '-legL" fill="none" stroke="' + INK + '" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path id="' + prefix + '-legR" fill="none" stroke="' + INK + '" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path id="' + prefix + '-torso" fill="none" stroke="' + INK + '" stroke-width="7" stroke-linecap="round"/>' +
      '<path id="' + prefix + '-armL" fill="none" stroke="' + INK + '" stroke-width="6.2" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<g id="' + prefix + '-handL"></g>' +
      '<path id="' + prefix + '-armR" fill="none" stroke="' + INK + '" stroke-width="6.2" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<g id="' + prefix + '-handR"></g>' +
      '<path id="' + prefix + '-collar" d="M154,212 Q178,226 204,212 L200,222 Q178,234 158,222 Z" fill="#9A4D2A" stroke="' + INK + '" stroke-width="4.2" stroke-linejoin="round"/>' +
      '<g id="' + prefix + '-medallion">' +
      '<circle id="' + prefix + '-med-bg" cx="178" cy="233" r="11.5" fill="#C5A059" stroke="' + INK + '" stroke-width="4"/>' +
      '<circle cx="174" cy="229" r="3" fill="#FEF3C7"/>' +
      "</g>" +
      // V1's crisp upright Owl Head silhouette (tall rounded crown + flared ear tufts + warm amber beak!)
      '<g id="' + prefix + '-head">' +
      '<path id="' + prefix + '-head-fill" d="M118,142 C114,104 128,82 114,58 C134,68 148,74 178,74 C208,74 222,68 242,58 C228,82 242,104 238,142 C238,186 212,214 178,214 C144,214 118,186 118,142 Z" fill="#FFFFFF" stroke="' + INK + '" stroke-width="6.2" stroke-linejoin="round"/>' +
      '<path id="' + prefix + '-cel-fill" d="M126,115 C119,154 134,196 172,208 C147,196 135,164 137,118 Z" fill="#E6E1D6"/>' +
      // Bright Wide Owl Eyes inside Glasses
      '<circle cx="152" cy="134" r="22.5" fill="#FFFFFF" stroke="' + INK + '" stroke-width="4.4"/>' +
      '<circle cx="204" cy="134" r="22.5" fill="#FFFFFF" stroke="' + INK + '" stroke-width="4.4"/>' +
      '<g clip-path="url(#' + prefix + '-eyeL-clip)">' +
      '<circle id="' + prefix + '-pupL" cx="147" cy="135" r="5.2" fill="' + INK + '"/>' +
      '<rect id="' + prefix + '-lidTL" x="124" y="76" width="56" height="32" fill="#FFFFFF" stroke="' + INK + '" stroke-width="3.6"/>' +
      '<rect id="' + prefix + '-lidBL" x="124" y="160" width="56" height="28" fill="#E5E7EB" stroke="' + INK + '" stroke-width="3"/>' +
      "</g>" +
      '<g clip-path="url(#' + prefix + '-eyeR-clip)">' +
      '<circle id="' + prefix + '-pupR" cx="199" cy="135" r="5.2" fill="' + INK + '"/>' +
      '<rect id="' + prefix + '-lidTR" x="176" y="76" width="56" height="32" fill="#FFFFFF" stroke="' + INK + '" stroke-width="3.6"/>' +
      '<rect id="' + prefix + '-lidBR" x="176" y="160" width="56" height="28" fill="#E5E7EB" stroke="' + INK + '" stroke-width="3"/>' +
      "</g>" +
      // Wireframe Glasses
      '<g id="' + prefix + '-glasses">' +
      '<circle cx="152" cy="134" r="26" fill="none" stroke="' + INK + '" stroke-width="3.5"/>' +
      '<circle cx="204" cy="134" r="26" fill="none" stroke="' + INK + '" stroke-width="3.5"/>' +
      '<path d="M177,131 Q180,127 183,131" fill="none" stroke="' + INK + '" stroke-width="3.5" stroke-linecap="round"/>' +
      '<line x1="117" y1="128" x2="126" y2="132" stroke="' + INK + '" stroke-width="3.4" stroke-linecap="round"/>' +
      '<line x1="230" y1="132" x2="239" y2="128" stroke="' + INK + '" stroke-width="3.4" stroke-linecap="round"/>' +
      "</g>" +
      // Expressive Brows
      '<path id="' + prefix + '-browL" fill="none" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>' +
      '<path id="' + prefix + '-browR" fill="none" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>' +
      // Open Mouth Cavity + Classic Amber Owl Beak (clearly visible!)
      '<path id="' + prefix + '-mouth-bg" fill="#1E293B" stroke="' + INK + '" stroke-width="3.6" stroke-linejoin="round"/>' +
      '<path id="' + prefix + '-tongue" fill="none" stroke="#F87171" stroke-width="3.2" stroke-linecap="round"/>' +
      '<polygon id="' + prefix + '-beak-top" points="169,151 187,151 178,167" fill="#F59E0B" stroke="' + INK + '" stroke-width="3.8" stroke-linejoin="round"/>' +
      "</g>" +
      '<g id="' + prefix + '-tremor"></g>' +
      '<g id="' + prefix + '-emote"></g>' +
      "</g></svg>";

    const $ = (suffix) => container.querySelector("#" + prefix + "-" + suffix);
    const els = {
      turb: $("turb"),
      whole: $("whole"),
      head: $("head"),
      headFill: $("head-fill"),
      celFill: $("cel-fill"),
      collar: $("collar"),
      medallion: $("medallion"),
      medBg: $("med-bg"),
      torso: $("torso"),
      legL: $("legL"),
      legR: $("legR"),
      armL: $("armL"),
      armR: $("armR"),
      handL: $("handL"),
      handR: $("handR"),
      pupL: $("pupL"),
      pupR: $("pupR"),
      lidTL: $("lidTL"),
      lidTR: $("lidTR"),
      lidBL: $("lidBL"),
      lidBR: $("lidBR"),
      glasses: $("glasses"),
      browL: $("browL"),
      browR: $("browR"),
      mouthBg: $("mouth-bg"),
      tongue: $("tongue"),
      beakTop: $("beak-top"),
      tremor: $("tremor"),
      emote: $("emote"),
    };

    function talkEnvelope(t) {
      const activeList = wordWindows.length ? wordWindows : talkWindows;
      let best = 0;
      for (let i = 0; i < activeList.length; i++) {
        const s = activeList[i][0];
        const e = activeList[i][1];
        const dur = Math.max(0.06, e - s);
        if (t >= s - 0.02 && t <= e + 0.02) {
          const edge = Math.min(0.05, dur * 0.35);
          const inK = clamp01((t - (s - 0.02)) / edge);
          const outK = clamp01(((e + 0.02) - t) / edge);
          const prog = clamp01((t - s) / dur);
          const wave = dur > 0.32
            ? 0.40 + 0.60 * Math.abs(Math.sin(prog * Math.PI * Math.max(2, Math.round(dur * 4.5))))
            : 0.35 + 0.65 * Math.sin(prog * Math.PI);
          const w = Math.min(inK, outK) * wave;
          if (w > best) best = w;
        }
      }
      return clamp01(best);
    }

    function blinkEnvelope(t) {
      const p = (t + 0.7) % 3.4;
      if (p < 0.18) {
        return Math.sin((p / 0.18) * Math.PI);
      }
      return 0;
    }

    function sampleRigState(t) {
      if (keyframes.length === 1 || t <= keyframes[0].at) {
        return { a: POSES[keyframes[0].pose], b: POSES[keyframes[0].pose], kHead: 1, kArmL: 1, kArmR: 1, squashDip: 0 };
      }
      let idx = 0;
      for (let i = 1; i < keyframes.length; i++) {
        if (t >= keyframes[i].at) idx = i;
      }
      if (idx === 0) {
        const kf0 = keyframes[0];
        return { a: POSES[kf0.pose], b: POSES[kf0.pose], kHead: 1, kArmL: 1, kArmR: 1, squashDip: 0 };
      }
      const prev = keyframes[idx - 1];
      const curr = keyframes[idx];
      const dur = curr.dur || 0.36;
      const localT = t - curr.at;
      const a = POSES[prev.pose];
      const b = POSES[curr.pose];

      const kHead = localT >= dur ? 1 : easeOutBack(localT / dur, 1.3);
      const kArmL = localT <= 0.04 ? 0 : (localT >= dur + 0.04 ? 1 : easeInOutCubic((localT - 0.04) / dur));
      const kArmR = localT <= 0.07 ? 0 : (localT >= dur + 0.07 ? 1 : easeInOutCubic((localT - 0.07) / dur));
      const dip = localT >= 0 && localT < 0.14 ? Math.sin((localT / 0.14) * Math.PI) : 0;

      return { a, b, kHead, kArmL, kArmR, squashDip: dip };
    }

    function samplePersona(t) {
      if (personas.length === 1 || t <= personas[0].at) {
        const p = PERSONAS[personas[0].role];
        return { head: p.headFill, cel: p.celFill, collar: p.collarFill, med: p.medallionFill };
      }
      let idx = 0;
      for (let i = 1; i < personas.length; i++) {
        if (t >= personas[i].at) idx = i;
      }
      if (idx === 0) {
        const p = PERSONAS[personas[0].role];
        return { head: p.headFill, cel: p.celFill, collar: p.collarFill, med: p.medallionFill };
      }
      const prev = PERSONAS[personas[idx - 1].role];
      const curr = PERSONAS[personas[idx].role];
      const dur = personas[idx].dur || 0.24;
      const k = easeInOutCubic((t - personas[idx].at) / dur);
      return {
        head: lerpHex(prev.headFill, curr.headFill, k),
        cel: lerpHex(prev.celFill, curr.celFill, k),
        collar: lerpHex(prev.collarFill, curr.collarFill, k),
        med: lerpHex(prev.medallionFill, curr.medallionFill, k),
      };
    }

    function sampleLookOffset(t) {
      let lx = 0, ly = 0;
      for (let i = 0; i < lookTargets.length; i++) {
        const lt = lookTargets[i];
        if (t >= lt.at) {
          const prev = i > 0 ? lookTargets[i - 1] : { x: 0, y: 0 };
          const k = easeInOutCubic((t - lt.at) / 0.25);
          lx = lerp(prev.x, lt.x, k);
          ly = lerp(prev.y, lt.y, k);
        }
      }
      return [lx, ly];
    }

    function sampleActiveEmote(t) {
      for (let i = 0; i < emotes.length; i++) {
        const em = emotes[i];
        if (t >= em.at && t <= em.end) {
          const enterK = easeOutBack((t - em.at) / 0.24, 1.45);
          const exitK = clamp01((em.end - t) / 0.16);
          return { kind: em.kind, scale: enterK * exitK, opacity: clamp01((t - em.at) / 0.12) * exitK, localT: t - em.at };
        }
      }
      return null;
    }

    let lastHandL = "";
    let lastHandR = "";
    let lastTremor = false;
    let lastEmoteKind = "";

    function render(t) {
      els.turb.setAttribute("seed", String(1 + (Math.floor(t * 12) % 7)));

      const st = sampleRigState(t);
      const { a, b, kHead, kArmL, kArmR, squashDip } = st;
      const idleBreath = Math.sin(t * 2.4) * 2.0;
      const idleSway = Math.sin(t * 1.45) * 1.3;

      const pStyle = samplePersona(t);
      els.headFill.setAttribute("fill", pStyle.head);
      els.celFill.setAttribute("fill", pStyle.cel);
      els.lidTL.setAttribute("fill", pStyle.head);
      els.lidTR.setAttribute("fill", pStyle.head);
      els.collar.setAttribute("fill", pStyle.collar);
      els.medBg.setAttribute("fill", pStyle.med);

      const sx = lerp(a.scaleX, b.scaleX, clamp01(kHead)) + squashDip * 0.05;
      const sy = lerp(a.scaleY, b.scaleY, clamp01(kHead)) - squashDip * 0.06;
      const shakeX = b.tremor && kHead > 0.7 ? Math.sin(t * 36) * 2.0 : 0;

      els.whole.setAttribute(
        "transform",
        "translate(" + (178 + shakeX).toFixed(1) + ",410) scale(" + sx.toFixed(3) + "," + sy.toFixed(3) + ") translate(-178,-410)"
      );

      const hRot = lerp(a.headRot, b.headRot, kHead) + idleSway * 0.5;
      const hX = lerp(a.headX, b.headX, kHead);
      const hY = lerp(a.headY, b.headY, kHead) + idleBreath * 0.7;
      els.head.setAttribute("transform", "translate(" + hX.toFixed(1) + "," + hY.toFixed(1) + ") rotate(" + hRot.toFixed(2) + " 178 214)");
      els.collar.setAttribute("transform", "translate(" + (hX * 0.6).toFixed(1) + "," + (hY * 0.7).toFixed(1) + ")");
      els.medallion.setAttribute("transform", "translate(" + (hX * 0.5).toFixed(1) + "," + (hY * 0.75 + Math.sin(t * 2.4 + 0.5) * 0.8).toFixed(1) + ")");

      const neckX = 178 + hX * 0.5;
      const neckY = 220 + hY * 0.7;
      const lean = lerp(a.torsoLean, b.torsoLean, clamp01(kHead));
      els.torso.setAttribute("d", "M" + neckX.toFixed(1) + "," + neckY.toFixed(1) + " Q" + lean.toFixed(1) + ",270 178,318");

      const lk = interpVec2(a.lKnee, b.lKnee, clamp01(kArmL));
      const lf = interpVec2(a.lFoot, b.lFoot, clamp01(kArmL));
      const rk = interpVec2(a.rKnee, b.rKnee, clamp01(kArmR));
      const rf = interpVec2(a.rFoot, b.rFoot, clamp01(kArmR));
      els.legL.setAttribute("d", "M170,315 L" + lk[0].toFixed(1) + "," + lk[1].toFixed(1) + " L" + lf[0].toFixed(1) + "," + lf[1].toFixed(1) + " L" + (lf[0] - 24).toFixed(1) + "," + lf[1].toFixed(1));
      els.legR.setAttribute("d", "M188,315 L" + rk[0].toFixed(1) + "," + rk[1].toFixed(1) + " L" + rf[0].toFixed(1) + "," + rf[1].toFixed(1) + " L" + (rf[0] + 24).toFixed(1) + "," + rf[1].toFixed(1));

      const lcp = interpVec2(a.lArmCP, b.lArmCP, kArmL);
      const lend = interpVec2(a.lArmEnd, b.lArmEnd, kArmL);
      els.armL.setAttribute("d", "M177," + (242 + idleBreath * 0.5).toFixed(1) + " Q" + lcp[0].toFixed(1) + "," + (lcp[1] + idleBreath).toFixed(1) + " " + lend[0].toFixed(1) + "," + (lend[1] + idleBreath * 0.7).toFixed(1));

      const rcp = interpVec2(a.rArmCP, b.rArmCP, kArmR);
      const rend = interpVec2(a.rArmEnd, b.rArmEnd, kArmR);
      els.armR.setAttribute("d", "M179," + (242 + idleBreath * 0.5).toFixed(1) + " Q" + rcp[0].toFixed(1) + "," + (rcp[1] + idleBreath).toFixed(1) + " " + rend[0].toFixed(1) + "," + (rend[1] + idleBreath * 0.7).toFixed(1));

      const hKindL = kArmL > 0.45 ? b.lHand : a.lHand;
      const hKindR = kArmR > 0.45 ? b.rHand : a.rHand;
      if (hKindL !== lastHandL) {
        els.handL.innerHTML = handMarkup(hKindL);
        lastHandL = hKindL;
      }
      if (hKindR !== lastHandR) {
        els.handR.innerHTML = handMarkup(hKindR);
        lastHandR = hKindR;
      }
      const lhr = lerp(a.lHandRot, b.lHandRot, kArmL);
      const rhr = lerp(a.rHandRot, b.rHandRot, kArmR);
      els.handL.setAttribute("transform", "translate(" + lend[0].toFixed(1) + "," + (lend[1] + idleBreath * 0.7).toFixed(1) + ") rotate(" + lhr.toFixed(1) + ")");
      els.handR.setAttribute("transform", "translate(" + rend[0].toFixed(1) + "," + (rend[1] + idleBreath * 0.7).toFixed(1) + ") rotate(" + rhr.toFixed(1) + ")");

      // Eyelids strictly clear of top clip edge (76+32 = 108 < 111.5) when open!
      const blink = blinkEnvelope(t);
      const topLid = Math.max(lerp(a.lidTop, b.lidTop, clamp01(kHead)), blink);
      const botLid = Math.max(lerp(a.lidBot, b.lidBot, clamp01(kHead)), blink * 0.85);
      els.lidTL.setAttribute("y", (76 + topLid * 58).toFixed(1));
      els.lidTR.setAttribute("y", (76 + topLid * 58).toFixed(1));
      els.lidBL.setAttribute("y", (160 - botLid * 26).toFixed(1));
      els.lidBR.setAttribute("y", (160 - botLid * 26).toFixed(1));

      const [lx, ly] = sampleLookOffset(t);
      const px = lerp(a.pupilX, b.pupilX, clamp01(kHead)) + lx;
      const py = lerp(a.pupilY, b.pupilY, clamp01(kHead)) + ly;
      const pr = lerp(a.pupilR, b.pupilR, clamp01(kHead));
      els.pupL.setAttribute("cx", (152 + px).toFixed(1));
      els.pupL.setAttribute("cy", (134 + py).toFixed(1));
      els.pupL.setAttribute("r", pr.toFixed(1));
      els.pupR.setAttribute("cx", (204 + px).toFixed(1));
      els.pupR.setAttribute("cy", (134 + py).toFixed(1));
      els.pupR.setAttribute("r", pr.toFixed(1));

      const bLY = lerp(a.browLY, b.browLY, clamp01(kHead)) - blink * 2;
      const bLA = lerp(a.browLAngle, b.browLAngle, clamp01(kHead));
      const bRY = lerp(a.browRY, b.browRY, clamp01(kHead)) - blink * 2;
      const bRA = lerp(a.browRAngle, b.browRAngle, clamp01(kHead));
      els.browL.setAttribute("d", "M132," + (bLY - bLA * 0.32).toFixed(1) + " Q152," + (bLY - 6).toFixed(1) + " 168," + (bLY + bLA * 0.32).toFixed(1));
      els.browR.setAttribute("d", "M188," + (bRY - bRA * 0.32).toFixed(1) + " Q204," + (bRY - 6).toFixed(1) + " 224," + (bRY + bRA * 0.32).toFixed(1));

      // Clear amber upper owl beak + active dark speech jaw beneath it
      const talk = talkEnvelope(t);
      const jawHold = lerp(a.jawBase, b.jawBase, clamp01(kHead));
      const openAmt = talk > 0.02
        ? clamp01(jawHold * 0.16 + talk * 0.90)
        : clamp01(jawHold * 0.85);

      const liftY = -openAmt * 2.5;
      els.beakTop.setAttribute(
        "points",
        "169," + (151 + liftY).toFixed(1) + " 187," + (151 + liftY).toFixed(1) + " 178," + (166 + liftY).toFixed(1)
      );
      if (openAmt > 0.06) {
        const drop = 160 + openAmt * 25;
        const hw = 7 + openAmt * 5;
        els.mouthBg.setAttribute(
          "d",
          "M" + (178 - hw).toFixed(1) + ",161 Q178," + drop.toFixed(1) + " " + (178 + hw).toFixed(1) + ",161 Q178,166 " + (178 - hw).toFixed(1) + ",161 Z"
        );
        els.mouthBg.setAttribute("opacity", "1");
        if (openAmt > 0.35) {
          els.tongue.setAttribute(
            "d",
            "M" + (178 - hw * 0.5).toFixed(1) + "," + (drop - 5).toFixed(1) + " Q178," + (drop - 9 * openAmt).toFixed(1) + " " + (178 + hw * 0.5).toFixed(1) + "," + (drop - 5).toFixed(1)
          );
          els.tongue.setAttribute("opacity", "1");
        } else {
          els.tongue.setAttribute("opacity", "0");
        }
      } else {
        els.mouthBg.setAttribute("opacity", "0");
        els.tongue.setAttribute("opacity", "0");
      }

      const showTremor = !!b.tremor && kHead > 0.55;
      if (showTremor !== lastTremor) {
        els.tremor.innerHTML = showTremor
          ? '<path d="M92,102 L86,118 L94,132 L86,148 M264,102 L270,118 L262,132 L270,148" fill="none" stroke="' + INK + '" stroke-width="3.4" stroke-linecap="round"/>'
          : "";
        lastTremor = showTremor;
      }

      const em = sampleActiveEmote(t);
      if (em) {
        if (em.kind !== lastEmoteKind) {
          els.emote.innerHTML = emoteMarkup(em.kind);
          lastEmoteKind = em.kind;
        }
        const bob = Math.sin(em.localT * 6.5) * 4.0;
        els.emote.setAttribute("opacity", em.opacity.toFixed(3));
        els.emote.setAttribute(
          "transform",
          "translate(178," + (24 + bob).toFixed(1) + ") scale(" + em.scale.toFixed(3) + ") translate(-178,-24)"
        );
      } else {
        if (lastEmoteKind) {
          els.emote.innerHTML = "";
          lastEmoteKind = "";
        }
        els.emote.setAttribute("opacity", "0");
      }
    }

    return { render };
  }

  global.ThinkLateEddyRig = { createEddyRig: createEddyRig };
})(window);
